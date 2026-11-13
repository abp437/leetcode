from typing import Protocol


class QuackBehavior(Protocol):
    def quack(self) -> None: ...
