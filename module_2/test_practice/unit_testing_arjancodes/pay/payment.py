from typing import Protocol

from pay.order import Order
from pay.processor import PaymentProcessor

# class PaymentProcessor(Protocol):
#     def charge(self, card: str, month: int, year: int, amount: int) -> None:
#         """Charges the card with given amount"""

def pay_order(order: Order, processor: PaymentProcessor) -> None:
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    card = input("Please enter your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    # payment_processor = PaymentProcessor("6cfb67f3-6281-4031-b893-ea85db0dce20")
    processor.charge(card, month, year, amount=order.total)
    order.pay()