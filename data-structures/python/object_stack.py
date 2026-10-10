from typing import Generic, TypeVar

T = TypeVar("T")


class ObjectStack(Generic[T]):
    def __init__(self) -> None:
        self.count = 0
        self.storage: dict[int, T] = {}

    def push(self, item: T) -> None:
        self.storage[self.count] = item
        self.count += 1

    def pop(self) -> T | None:
        if self.count == 0:
            return None

        last_elem = self.storage[self.count - 1]
        del self.storage[self.count - 1]
        self.count -= 1
        return last_elem

    @property
    def size(self) -> int:
        return self.count

    @property
    def peek(self) -> T | None:
        if self.count == 0:
            return None

        return self.storage[self.count - 1]
