from dataclasses import dataclass

@dataclass
class CreditCard:
    card_number: str
    expiry_month: int
    expiry_year: int