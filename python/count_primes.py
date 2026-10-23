# There's a much more efficient way of counting primes by only checking the prime divisors and marking multiples of primes and composite, so no need to check using Sieve of Eratosthenes
def count_primes(n: int) -> int:
    count = 1
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        for num in range(3, n, 2):
            square_root = int(num**0.5) + 1
            for inner_num in range(3, square_root, 2):
                if num != inner_num and num % inner_num == 0:
                    break
            else:
                count += 1
    return count


num: int = int(input("Enter the number until which primes to count: "))

print(f"Prime numbers until {num} are: {count_primes(num)}")
