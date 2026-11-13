from behaviors.flying.fly_behavior import FlyBehavior
from behaviors.quacking.quack_behavior import QuackBehavior


class Duck:
    def __init__(
        self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior
    ) -> None:
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self) -> None:
        print("I'm Super Duck Swimming")

    def display(self) -> None:
        print("I'm Super Duck")

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self.quack_behavior = quack_behavior
