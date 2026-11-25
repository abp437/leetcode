from progression import Progression


class AbsoluteProgression(Progression):
    def __init__(self, start: int = 0, increment_factor: int = 1) -> None:
        super().__init__(abs(start))
        self.increment_factor = increment_factor

    def advance(self) -> None:
        self.current += self.increment_factor

    def print_progression(self, count: int) -> None:
        count = abs(count)

        super().print_progression(count)


if __name__ == "__main__":
    progression = AbsoluteProgression(-13, 12)
    progression.print_progression(-5)
