I don't have evidence of your prior work with Python concurrency specifically, so I'll cover `asyncio` task cancellation directly while briefly defining prerequisite concepts inline. If any term feels unfamiliar, flag it and I'll expand on that point.

## Core Mechanism

A `Task` is a wrapper that schedules a coroutine on the event loop. Calling `task.cancel()` **does not** immediately interrupt the coroutine. Instead, it schedules a `CancelledError` to be raised at the **next `await` expression** inside that coroutine.

```python
import asyncio

async def worker():
    print("start")
    await asyncio.sleep(5)  # CancelledError injected here
    print("never reached")

async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(0.1)  # let worker start
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("task was cancelled")

asyncio.run(main())
```

**Output:**
```
start
task was cancelled
```

Key point: if the coroutine is executing synchronous CPU-bound code (no `await`), cancellation is deferred until the next suspension point.

## Cleanup Guarantee

Use `try/finally` or `async with` to ensure resources are released even when cancelled:

```python
async def worker():
    conn = await acquire_connection()
    try:
        while True:
            await conn.ping()
            await asyncio.sleep(1)
    finally:
        await conn.close()  # always runs
```

## Shielding

`asyncio.shield()` protects an inner task from external cancellation. The shielded task itself can still finish or fail normally, but a cancel aimed at the caller won't propagate into it:

```python
task = asyncio.create_task(asyncio.shield(inner_task))
# later: task.cancel()  # cancels the shield wrapper, inner_task keeps running
```

Use this when the inner operation must commit (e.g., a database write) even if the caller times out.

## Timeouts

Python 3.11+ introduced `asyncio.timeout()` as the modern pattern:

```python
async def main():
    try:
        async with asyncio.timeout(5):
            await slow_operation()
    except TimeoutError:
        print("timed out")
```

Under the hood, this creates a cancel scope: if the block exceeds 5 seconds, the current task receives `CancelledError`. The legacy equivalent is `asyncio.wait_for(slow_operation(), timeout=5)`, which wraps the coroutine in a new Task and cancels it on timeout.

## Common Pitfall: Swallowing `CancelledError`

Never catch `CancelledError` silently. If you must catch it, always re-raise:

```python
# Bad
try:
    await task
except asyncio.CancelledError:
    pass  # task appears done; asyncio internals break

# Good
try:
    await task
except asyncio.CancelledError:
    await cleanup()
    raise  # mandatory
```

Swallowing it confuses the event loop's task bookkeeping and can suppress cancellation in parent scopes (e.g., `TaskGroup` in 3.11+).

## TaskGroup Cancellation (3.11+)

In a `TaskGroup`, if one child task raises an exception (including via cancellation), all sibling tasks are automatically cancelled:

```python
async with asyncio.TaskGroup() as tg:
    tg.create_task(task_a())
    tg.create_task(task_b())  # if task_a raises, task_b is cancelled
```

This is the modern replacement for manually gathering and cancelling tasks.

---

If any of these concepts—`Task`, `create_task`, the event loop, or `await` suspension—need clarification before the cancellation behavior makes sense, let me know which one.
