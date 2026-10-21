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

    # Overrides the default way of displaying the object in CLI.
    # Instead of showing pointer to object, we provide a custom string to represent it.
    def __repr__(self) -> str:
        return self.name

    def apply_discount(self) -> None:
        self.price = round((self.price - (self.price * self.discount_rate)), 2)

    def calculate_price(self) -> float:
        return self.price * self.quantity


item = Item("Phone", 75.02, 3)

print(type(item))
print(type(item.price))
print(type(item.quantity))
print(type(item.name))
print(item.price)
print(item.calculate_price())

print("hello".upper())
print("hello".isalnum())

# Class variables
print(Item.discount_rate)
item.apply_discount()
print(item.price)

item2 = Item("Table", 22321, 5)
# This change doesn't apply for the full class, it applies only to this instance
# Subsequent instances will pick up values from the class variable itself
item2.discount_rate = 0.3
item2.apply_discount()
print(item2.price)

item3 = Item("Chair", 383, 8)
item3.apply_discount()
print(item3.price)

print(Item.all)

for inst in Item.all:
    print(inst.name)

# Testing type & value validations
# item4 = Item("TV", -23, -35)
# print(item4.calculate_price())


Item.instantiate_from_csv()
print(Item.all)
