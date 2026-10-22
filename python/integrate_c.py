import ctypes

lib = ctypes.CDLL("./basic_calc.so")

# Configure argument and return types
# For dividing we need to specifically set the return type to float, the default return type is int in C libraries.
lib.divide.argtypes = [ctypes.c_int, ctypes.c_int]
lib.divide.restype = ctypes.c_float

print(f"=> {lib.add(10, 20)}")
print(f"=> {lib.multiply(10, 20)}")
print(f"=> {lib.subtract(10, 20)}")
print(f"=> {lib.divide(10, 20)}")
print(f"=> {lib.modulo(10, 20)}")

print(f"=> {lib.add(137, 286)}")
print(f"=> {lib.multiply(143, 267)}")
print(f"=> {lib.subtract(583, 749)}")
print(f"=> {lib.divide(847, 23)}")
print(f"=> {lib.modulo(937, 64)}")

print(f"=> {lib.add(1247, 3896)}")
print(f"=> {lib.multiply(317, 429)}")
print(f"=> {lib.subtract(4821, 7654)}")
print(f"=> {lib.divide(7634, 137)}")
print(f"=> {lib.modulo(8765, 342)}")
