n = 5
tree = [0] * (n + 1)

''' Fenwick Tree (Binary Indexed Tree) '''
def update(i, dif):
    global n
    while i <= n:
        tree[i] += dif
        i += (i & -i)

def update_to(i, to):
    update(i, to - interval_sum(i, i))

def get_sum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

def interval_sum(start, end):
    return get_sum(end) - get_sum(start - 1)

# Set all the data input
update_to(1, 1)
update_to(2, 2)
update_to(3, 3)
update_to(4, 4)
update_to(5, 5)
# Interval sum from index 2 to index 5.
print(interval_sum(2, 5))
# Update index 3.
update(3, -2)
# Interval sum from index 2 to index 5.
print(interval_sum(2, 5))
# Update index 5.
update(5, 2)
# Interval sum from index 2 to index 5.
print(interval_sum(2, 5))
# Interval sum from index 1 to index 5.
print(interval_sum(1, 5))
