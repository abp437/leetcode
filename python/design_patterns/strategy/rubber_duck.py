from behaviors.flying.no_fly import NoFly
from behaviors.quacking.squeak import Squeak
from duck import Duck


class RubberDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behavior=NoFly(), quack_behavior=Squeak())

    def display(self) -> None:
        print("I'm Rubber Duck")

    def quack(self) -> None:
        print("I'm a Rubber Duck and I can Squeak, but can't Quack")
