import math

''' Find all divisors of a number '''
def find_all_divisors_of_a_number(x):
    result = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            result.append(i)
            if i * i != x:
                result.append(x // i)
    return result

print(find_all_divisors_of_a_number(12)) # [1, 12, 2, 6, 3, 4]
