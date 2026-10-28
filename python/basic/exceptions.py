try:
    a = 10 / 0
    b = 10 + "a"
    print("Appa!")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
except TypeError as t:
    print(f"TypeError: {t}")
except Exception as e:
    print(f"Generic Exception: {e}")
else:
    print("No exception occurred")
finally:
    print("Finally Cleaning up")

print("After exception handling")


class ValueTooHigh(Exception):
    def __init__(self, message, value) -> None:
        self.message = message
        self.value = value


def test_value(v) -> ValueTooHigh | None:
    if v > 20:
        raise ValueTooHigh("Value is tooo high", v)


try:
    a = 20
    b = 100
    test_value(a)
    test_value(b)
except ValueTooHigh as v:
    print(f"From Custom Exception Handling: {v}")
