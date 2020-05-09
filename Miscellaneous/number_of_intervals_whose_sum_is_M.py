''' Find the number of intervals whose sum is M (using the two-pointer method). '''
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# move 'start' pointer to the right.
for start in range(n):
    # move 'end' pointer to the right.
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # If the sum of interval is 'm', count the number.
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
