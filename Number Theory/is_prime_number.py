import math

''' Check if a number is prime '''
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True
