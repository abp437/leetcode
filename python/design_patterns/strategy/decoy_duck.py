from behaviors.flying.no_fly import NoFly
from behaviors.quacking.no_quack import NoQuack
from duck import Duck


class DecoyDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behavior=NoFly(), quack_behavior=NoQuack())

    def display(self) -> None:
        print("I'm Decoy Duck")

    def quack(self) -> None:
        print("I can't quack man")
