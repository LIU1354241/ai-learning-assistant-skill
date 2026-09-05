Yes. Your prior Python experience is enough to skip general syntax, but it doesn’t establish Python concurrency knowledge, so I’ll introduce only the concurrency concepts needed as they arise.

In `asyncio`, cancellation is a request, not an immediate forced stop:

```python
import asyncio

async def worker():
    try:
        while True:
            await asyncio.sleep(1)
    finally:
        print("cleanup completed")

async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(0.1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("task cancelled")

asyncio.run(main())
```

`task.cancel()` arranges for `asyncio.CancelledError` to be raised inside the coroutine, usually at its next `await`. Awaiting the cancelled task lets its cleanup finish and confirms the outcome. Put cleanup in `finally`; if you catch `CancelledError` inside the coroutine, generally re-raise it after cleanup so cancellation can propagate.
