class Progression:
    def __init__(self, start: int = 0) -> None:
        self.current = start

    def advance(self) -> None:
        self.current += 1

    def next_val(self) -> int:
        self.advance()
        return self.current

    def print_progression(self, count: int) -> None:
        if count <= 0:
            print("Provide a value greater than 0 to progress")
            return

        print(self.current)
        for _ in range(count - 1):
            print(self.next_val())


if __name__ == "__main__":
    progression = Progression(10)
    progression.print_progression(-5)
