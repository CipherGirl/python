import pytest

from pay.order import LineItem, Order
from pay.payment import pay_order
from pytest import MonkeyPatch


class PaymentProcessorMock:
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        print(f"Charged {amount} on {card}")

def test_pay_order(monkeypatch: MonkeyPatch) -> None:

    inputs = ["1249190007575069", 12, 2026]

    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    order = Order()
    order.line_items.append(LineItem("Test", 200))
    pay_order(order, PaymentProcessorMock())

def test_pay_order_invalid(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", 12, 2026]

        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

        order = Order()
        pay_order(order, PaymentProcessorMock())