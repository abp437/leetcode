from progression import Progression


class GeometricProgression(Progression):
    def __init__(self, start: int = 0, increment_factor: int = 1) -> None:
        super().__init__(start)
        self.increment_factor = max(increment_factor, 1)

    def advance(self) -> None:
        self.current *= self.increment_factor


if __name__ == "__main__":
    progression = GeometricProgression(-13, 4)
    progression.print_progression(6)
