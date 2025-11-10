# Don’t force a class to implement methods it doesn’t nee

"""Bad Example
from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def place_order(self):
        pass
        
    @abstractmethod
    def manage_orders(self):
        pass 
"""

from abc import ABC, abstractmethod

class ShopperActions(ABC):
    @abstractmethod
    def place_order(self):
        pass


class AdminActions(ABC):
    @abstractmethod
    def manage_orders(self):
        pass


class Customer(ShopperActions):
    def add_to_cart(self):
        print("Added item to cart")


class Admin(AdminActions):
    def manage_users(self):
        print("User managed")


"""
💡 Simple Explanation:

“Each role implements only what it needs. 
ISP prevents large, bloated interfaces that force unnecessary methods.”
"""