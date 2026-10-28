from itertools import product

a = [1, 3, 4]
b = [377, 29, 48]

# Computes the cartesian product of 2 lists
# Basically, it doesn't do multiplication or anything, it just iterates over lists in a cartesian manner
result = product(a, b)
print(type(result))
print(result)

for x in result:
    first, second = x
    print(f"{first}, {second} = {first * second}")

# The main difference between permutations and combinations is whether the order of selection matters.
# Permutation: Order matters.
# Combination: Order does not matter.
