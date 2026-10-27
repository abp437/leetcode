# Tuples are immutable
import sys

my_tuple = ("Max", 27, "Boston", "Nairobi", "Tokyo", "Helsinki", "Professor")
my_list = ["Max", 27, "Boston", "Nairobi", "Tokyo", "Helsinki", "Professor"]

print(type(my_tuple))
print(my_tuple[2])
print(my_tuple.count("Appa"))

# The below assignment throws an error, that's why put up in try-except
try:
    my_tuple[2] = "Appa"
except TypeError as e:
    print(f"TypeError: {e}")

print("After")

# Check existence of an element in Tuple
print("Present" if "Max" in my_tuple else "Not Present")
print(f"List size with same elements: {sys.getsizeof(my_list)}")
print(f"Tuple size with same elements: {sys.getsizeof(my_tuple)}")
