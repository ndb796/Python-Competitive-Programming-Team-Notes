x = 24
y = 32

''' GCD (Greatest Common Divisor) '''
def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

print(gcd(x, y))
