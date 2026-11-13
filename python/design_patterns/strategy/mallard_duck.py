from behaviors.flying.fly_with_wings import FlyWithWings
from behaviors.quacking.quack import Quack
from duck import Duck


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__(fly_behavior=FlyWithWings(), quack_behavior=Quack())

    def display(self) -> None:
        print("I'm Mallard Duck")
