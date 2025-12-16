from platform import processor

from pay.processor import PaymentProcessor
from pay.card import CreditCard
import pytest

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

@pytest.fixture
def card() -> CreditCard:
    return CreditCard("1249190007575069", 12, 2026)


def test_api_key_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge(card,100)

def test_card_valid_date(card: CreditCard) -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card, 100)

def test_card_invalid_date(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        card = CreditCard("1249190007575069", 12, 1900)
        processor.charge(card, 100)

def test_card_valid(card: CreditCard) -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card, 100)

def test_card_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        card = CreditCard("INVALID", 12, 1900)
        processor.charge(card, 100)