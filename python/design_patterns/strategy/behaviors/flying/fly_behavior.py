from typing import Protocol


class FlyBehavior(Protocol):
    """
    Any class providing a compatible fly() method
    structurally satisfies this Protocol.

    This is Python's way of defining an interface
    using structural subtyping (duck typing).
    """

    def fly(self) -> None: ...
