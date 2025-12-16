from pay.order import Order, LineItem, OrderStatus


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0

def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test Product", price=200))
    assert order.total == 200

def test_order_multiple_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test Product 1", price=200))
    order.line_items.append(LineItem(name="Test Product 2", price=500))
    assert order.total == 700

def test_order_pay() -> None:
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID