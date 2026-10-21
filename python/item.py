import csv
from typing import ClassVar


class Item:
    discount_rate: float = 0.15
    all: ClassVar[list["Item"]] = []

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        # Type Validations
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number")

        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        # Value Validations
        if not (price >= 0):
            raise ValueError(f"{price} must be greater than or equal to 0")

        if not (price >= 0):
            raise ValueError(f"{quantity} must be greater than or equal to 0")

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("./items.csv", newline="") as csvfile:
            items = csv.DictReader(csvfile, delimiter=",")
            for row in items:
                name = row.get("name")
                price = row.get("price")
                quantity = row.get("quantity")

                if name is None or price is None or quantity is None:
                    raise ValueError("Missing required CSV field")

                cls(name, float(price), int(quantity))

    @staticmethod
    def is_int(num) -> bool:
        return isinstance(num, int)

    # Overrides the default way of displaying the object in CLI.
    # Instead of showing memory address of the object, we provide a custom string to represent it.
    # Similar is the __str__ dunder method, but the __str__ has got more preference with the __repr__ as fallback
    def __repr__(self) -> str:
        return f"From repr: {self.name}"

    def __str__(self) -> str:
        return f"From str: {self.name}, {self.price}, {self.quantity}"

    # This method will operate when we try to add 2 objects using the + operator of this class to each other
    def __add__(self, other) -> str:
        return f"{self.name} + {other.name}"

    def apply_discount(self) -> None:
        self.price = round((self.price - (self.price * self.discount_rate)), 2)

    def calculate_price(self) -> float:
        return self.price * self.quantity


phone = Item("Phone", 75.02, 3)

print(type(phone))
print(type(phone.price))
print(type(phone.quantity))
print(type(phone.name))
print(phone.price)
print(phone.calculate_price())

print("hello".upper())
print("hello".isalnum())

# Class variables
print(Item.discount_rate)
phone.apply_discount()
print(phone.price)

table = Item("Table", 22321, 5)
# This change doesn't apply for the full class, it applies only to this instance
# Subsequent instances will pick up values from the class variable itself
table.discount_rate = 0.3
table.apply_discount()
print(table.price)

chair = Item("Chair", 383, 8)
chair.apply_discount()
print(chair.price)

print(chair + table)

# This will call the __repr__
print(Item.all)


for inst in Item.all:
    # This will call the __str__
    print(inst)

Item.instantiate_from_csv()
# This will call the __repr__
print(Item.all)

print(Item.is_int("2"))

# Testing type & value validations
testing = Item("TV", -23, -35)
print(testing.calculate_price())
