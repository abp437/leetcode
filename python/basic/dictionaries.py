# Literal declaration
person = {
    "name": "Akshay",
    "age": 32,
    "programming_languages": ["Python", "TypeScript", "Go", "C++"],
    32: "Expanding company, skills",
}

# We don't really need a loop to print the full dictionary
# But if we want to iterate, then this is how we do it
for key, value in person.items():
    print(f"{key}: {value}")

# Only iterate over values:
for value in person.values():
    print(value)
# Similarly we can iterate over keys as well.

# Searches for key in object
print("name" if "name" in person else "no name")

# With dictionary constructor
# Supports only string keys. Thus, literal declaration is preferred.
# But generally we prefer string keys only.
new_person = dict(name="Prajkta", age=27, programming_languages=[])

# Access happens with:
print(new_person["name"])

# Adding elements
new_person["email"] = "real_email@gmail.com"

# Prints full dictionary
print(new_person)

# Removing elements
del new_person["email"]

print(new_person)

# Dictionaries, just like lists are pass by reference. We need to create a copy using the `copy` function.
copy_person = new_person.copy()
print(f"Before merge: {copy_person}")

# We can even merge dictionaries
# But the clashing key-value pairs are replaced with the latest one
copy_person.update(person)
print(f"After merge: {copy_person}")
