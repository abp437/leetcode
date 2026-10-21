class Item:
    discount_rate: float = 0.25

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

    def calculate_price(self) -> float:
        return self.price * self.quantity


item = Item("Phone", 75.02, 3)

print(type(item))
print(type(item.price))
print(item.price)
print(item.calculate_price())
print(type(item.quantity))
print(type(item.name))

print("hello".upper())
print("hello".isalnum())

# Testing type & value validations
item2 = Item("TV", -23, -35)
print(item2.calculate_price())
