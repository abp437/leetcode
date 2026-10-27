st = "       Hello, World!   "

# Strings are immutable
print(st.strip())
print(st)

# To convert a string to a list, we use string splitting
print(st.strip().split())

# Similarly, if we want to join a string we generally use the below syntax
my_list: list[str] = ["hey", "there"]

# Joins a string with , as the delimiter
# Joining strings is a very essential use case for overall Python code
print(",".join(my_list))
