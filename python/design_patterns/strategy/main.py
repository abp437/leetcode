from behaviors.flying.fly_with_wings import FlyWithWings
from behaviors.quacking.squeak import Squeak
from decoy_duck import DecoyDuck
from mallard_duck import MallardDuck
from redhead_duck import RedheadDuck
from rubber_duck import RubberDuck


def main() -> None:
    ducks = [MallardDuck(), RedheadDuck(), RubberDuck(), DecoyDuck()]

    for duck in ducks:
        duck.display()
        duck.perform_fly()
        duck.perform_quack()

    print("=====================")
    decoy = ducks[-1]
    decoy.display()
    decoy.perform_fly()
    decoy.perform_quack()
    print("I'm changing behavior")
    decoy.set_fly_behavior(FlyWithWings())
    decoy.set_quack_behavior(Squeak())
    decoy.perform_fly()
    decoy.perform_quack()
    print("=====================")


if __name__ == "__main__":
    main()
