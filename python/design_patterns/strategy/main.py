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


if __name__ == "__main__":
    main()
