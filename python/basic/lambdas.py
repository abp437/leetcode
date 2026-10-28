from collections.abc import Callable

# Single Arg
add10: Callable[[int], int] = lambda x: x + 10

# We annotate using Callable, the first data type being the argument and the next being the return type
multiply_by_pi: Callable[[int], float] = lambda x: x * 3.14

# Multiple args
square_of_sum: Callable[[int, int], int] = lambda x, y: (x**2) + (2 * x * y) + (y**2)

print(add10(35))
print(multiply_by_pi(23))
print(square_of_sum(12, 22))


# Map
a = [12, 34, 5, 6, 7]
b = [1, 2, 3, 4, 9, 8]

# Map is very similar to the map function in JS
# Map function takes in a lambda function to operate and a list upon which the lambda function will operate
new_map = map(lambda x: x + 21, a)
print(type(new_map))

for el in new_map:
    print(el)

print(list(new_map))

new_filter = filter(lambda x: x > 3, b)
print(list(new_filter))

# List comprehension
c = [x for x in a if x % 2 == 0]
print(c)
