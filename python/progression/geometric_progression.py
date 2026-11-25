from progression import Progression


class GeometricProgression(Progression):
    def __init__(self, start: int = 0, multiply_factor: int = 1) -> None:
        super().__init__(start)
        self.multiply_factor = max(multiply_factor, 1)

    def advance(self) -> None:
        self.current *= self.multiply_factor


if __name__ == "__main__":
    progression = GeometricProgression(-13, 4)
    progression.print_progression(6)
