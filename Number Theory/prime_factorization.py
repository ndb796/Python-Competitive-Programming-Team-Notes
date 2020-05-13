import math

''' Get all the prime factors '''
def prime_factorization(x):
    result = []
    for i in range(2, int(math.sqrt(x)) + 1):
        # If 'i' is a divisor of 'x',
        if x % i == 0:
            # Count how many times 'i' can divide 'x' consecutively.
            count = 0
            while x % i == 0:
                count += 1
                x //= i
            result.append((i, count))
    if x > 1:
        result.append((x, 1))
    return result

# Note: 1 is neither a prime number (소수) nor a composite number (합성수).
print(prime_factorization(32)) # [(2, 5)]
print(prime_factorization(45)) # [(3, 2), (5, 1)]
print(prime_factorization(75)) # [(3, 1), (5, 2)]
