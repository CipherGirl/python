from typing import Protocol

from pay.card import CreditCard
from pay.order import Order


class PaymentProcessor(Protocol):
    def charge(self, card: CreditCard, amount: int) -> None:
        """Charge the card."""


def pay_order(
    order: Order, card: CreditCard, payment_processor: PaymentProcessor
) -> None:
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    payment_processor.charge(card, amount=order.total)
    order.pay()