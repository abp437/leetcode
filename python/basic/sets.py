the_rock_says: set[str] = {
    "Jabroni",
    "beating",
    "Pie",
    "eating",
    "trailblazing",
    "eyebrow raising",
    "Heart Stopping",
}

# To add
the_rock_says.add("Brahma Bull")

# To remove
the_rock_says.discard("Heart Stopping")

print("Andre the Giant" if "Brahma Bull" in the_rock_says else "All over Atlanta")

odds: set[int] = {1, 3, 5, 7, 9}
evens: set[int] = {2, 4, 6, 8}
primes: set[int] = {2, 3, 5, 7}

print(primes.intersection(odds))

just_nums = {12, 34, 586, 28}

# We can even merge sets like we merge dictionaries
just_nums.update(primes)
print(just_nums)
