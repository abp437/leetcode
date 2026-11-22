from abc import ABC, abstractmethod


# ABC - Indicates it inherits from Abstract Base Class
class Counter(ABC):
    @abstractmethod
    def increment(self, amount: int = 1) -> None:
        pass

    @property
    @abstractmethod
    def count(self) -> int:
        pass


class SimpleCounter(Counter):
    def __init__(self, initial: int = 0) -> None:
        self._count = initial

    def increment(self, amount: int = 1) -> None:
        self._count += amount

    @property
    def count(self) -> int:
        return self._count


class BoundedCounter(Counter):
    def __init__(self, initial: int = 0, maximum: int = 100) -> None:
        if initial > maximum:
            raise ValueError("Initial count cannot exceed maximum")

        self._count = initial
        self._maximum = maximum

    def increment(self, amount: int = 1) -> None:
        self._count = min(self._count + amount, self._maximum)

    @property
    def count(self) -> int:
        return self._count


# Usage
counters: list[Counter] = [SimpleCounter(10), BoundedCounter(10, maximum=12)]

for counter in counters:
    counter.increment(5)
    print(type(counter).__name__, counter.count)
