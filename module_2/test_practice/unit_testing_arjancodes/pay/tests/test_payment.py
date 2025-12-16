import pytest

from pay.card import CreditCard
from pay.order import LineItem, Order
from pay.payment import pay_order
from pytest import MonkeyPatch


class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charged {amount} on {card.card_number}")

@pytest.fixture
def card() -> CreditCard:
    return CreditCard("1249190007575069", 12, 2026)

def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem("Test", 200))
    pay_order(order, card, PaymentProcessorMock())

def test_pay_order_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", 12, 2026]

        order = Order()
        pay_order(order, card, PaymentProcessorMock())