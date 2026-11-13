from typing import Protocol


class FlyBehavior(Protocol):
    def fly(self) -> None: ...
