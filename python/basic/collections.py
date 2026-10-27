from collections import Counter, defaultdict, deque, namedtuple

my_chars = "Appancha Vishay lay hard aahe"
char_counts = Counter(my_chars)
print(char_counts)
print(type(char_counts))

# Prints the 2 most common characters in the string
print(char_counts.most_common(2))

# Named tuple creates a custom class which can hold only those specified elements in it
# Below, we are creating a Point class which will accept only 3 values and we can access them like that only
# We can't add methods or anything which we typically add to any class
# That's why we call it as named tuple.
Point = namedtuple("Point", "x,y,z")
pt = Point(1, 3, 4)
print(pt)
print(type(pt))
print(f"x: {pt.x}, y: {pt.y}")

# Whenever we try to access items which are not a part of the dictionary we get KeyError
# But with defaultdict, we get a fallback value in return if a key is not present
# Otherwise we would have to put up the usual try-except blocks in it
d = defaultdict(str)

# A Deque is a double ended queue
de = deque()
# Enqueue at end
de.append(1)
de.append(2)
de.append(3)
de.append(4)
# Enqueue at beginning
de.appendleft(2)
de.appendleft(13)
de.appendleft(29)
de.appendleft(1)
# Dequeue from beginning
hello = de.popleft()
# Dequeue from left
hello_new = de.pop()
print(hello)
print(hello_new)
print(de)

# Multiple elements appended
de.extend([4, 2, 34, 45])

# Multiple elements prepended
de.extendleft([7823, 378])
print(de)
