import functools


# Decorator function
def mydecorator(func):
    def wrapper():
        print("Executing decorator before function")
        func()
        print("Executing decorator after function")

    return wrapper


@mydecorator
def dosomething():
    print("Hello, World!")


dosomething()


# Decorators with arguments and return values
def decorator_with_args(func):
    # The below line preserves the original function's name, docstring, and other metadata.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello, World!")
        result = func(*args, **kwargs)
        print("The World Ends!")
        return result

    return wrapper


@decorator_with_args
def execute_decorator(a: int, b: int) -> int:
    return a * b


print(execute_decorator(2, 7))
print(execute_decorator.__name__)


# Actually useful decorator
def repeat_times(num_of_times: int):
    if type(num_of_times) is not int or num_of_times < 1:
        raise ValueError("num_of_times must be a positive integer")

    def decorator_repeat(func):
        # The below line preserves the original function's name, docstring, and other metadata.
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_of_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat_times(num_of_times=4)
def hello(appa: int):
    print(appa * 23)


hello(76)
