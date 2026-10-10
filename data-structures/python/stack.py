from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T | None:
        if not self.items:
            return None
        return self.items.pop()

    def peek(self) -> T | None:
        if not self.items:
            return None
        return self.items[-1]

    @property
    def length(self) -> int:
        return len(self.items)
