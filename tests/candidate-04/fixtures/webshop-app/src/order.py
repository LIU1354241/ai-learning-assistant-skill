def processOrder(cart):
    """创建订单：校验购物车 -> 计算总价 -> 生成订单号。"""
    if not cart:
        return None
    total = sum(item["price"] * item["qty"] for item in cart)
    return {"order_id": "ORD-0001", "total": total}
