fruits: list[str | int | bool] = ["Apple", "Banana", "Orange", 45, True]
print(fruits)

# Getting to know if item present in list
print("There's a banana" if "banana" in fruits else "No banana")

"""
Some list methods
"""

# Appends at last as usual
fruits.append("Guava")

# Inserts at specific index
fruits.insert(1, "Pomogranate")
# Inserts at second last place, not the last one
fruits.insert(-1, "Pomogranate")
# Removes the first occurence of an element
fruits.remove("Pomogranate")

try:
    fruits.remove("Cashewnut")
except ValueError as e:
    print(f"Custom ValueError: {e}")

print("Program working even after  error")

nums: list[int] = [1, 3, 41, -192, 282, 28, 46]
print(f"Before sort: {nums}")

# This method actually changes the list. It's mutating
nums.sort()
print(f"After sort: {nums}")

# Even this method as well
nums.reverse()
print(f"After reverse: {nums}")

# Reversing a list without mutating
reversed_nums = nums[::-1]
print(reversed_nums)

# Assigning one list to another is pass by reference.
same_nums = reversed_nums
reversed_nums.remove(28)
print(same_nums)

# To create a true copy we need to do something like this:
new_nums = same_nums[:]
print(new_nums)
new_nums.remove(46)
print(new_nums)
print(same_nums)
