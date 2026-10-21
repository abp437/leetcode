import csv
from typing import ClassVar


class Item:
    discount_rate: float = 0.15
    all: ClassVar[list["Item"]] = []

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        # Type Validations
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number")

        # Value Validations
        if not (price >= 0):
            raise ValueError(f"{price} must be greater than or equal to 0")

        if not (price >= 0):
            raise ValueError(f"{quantity} must be greater than or equal to 0")

        # The line below will call the setter method
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls) -> None:
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

    # Getter method
    @property
    def name(self) -> str:
        return self.__name

    # Setter method
    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value

    # Overrides the default way of displaying the object in CLI.
    # Instead of showing memory address of the object, we provide a custom string to represent it.
    # Similar is the __str__ dunder method, but the __str__ has got to be more user friendly and __repr__ more dev friendly
    def __repr__(self) -> str:
        return f"From repr: {self.__name}"

    def __str__(self) -> str:
        return f"From str: {self.__name}, {self.price}, {self.quantity}"

    # This method will operate when we try to add 2 objects using the + operator of this class to each other
    def __add__(self, other) -> str:
        return f"{self.__name} + {other.name}"

    def apply_discount(self) -> None:
        self.price = round((self.price - (self.price * self.discount_rate)), 2)

    def calculate_price(self) -> float:
        return self.price * self.quantity
