number: int = int(input("Enter a number to check if prime: "))

if number < 2:
    print("Neither Prime or Composite")
elif number == 2:
    print("Is Prime")
elif number % 2 == 0:
    print("Is Composite")
else:
    # We only need to check until the square root of the number, that's the rule of checking primes.
    # There's a much more efficient way of checking primes by only checking the prime divisors using Sieve of Eratosthenes
    square_root = int(number**0.5) + 1
    for n in range(3, square_root, 2):
        if number % n == 0:
            print("Is Composite")
            break
    else:
        print("Is Prime")
