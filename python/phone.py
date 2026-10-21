from item import Item


class Phone(Item):
    """
    Inherits from the Item class.
    We just get those attributes inside our class automatically.
    """

    def __init__(self, price: float, quantity: int = 0, is_broken=False) -> None:
        super().__init__("Phone", price, quantity)
        self.is_broken = is_broken

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, is_broken: {self.is_broken}, quantity: {self.quantity}"
