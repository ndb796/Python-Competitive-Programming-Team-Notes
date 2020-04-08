n = 10
target = 13
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

''' Binary Search (Iterative Method) '''
def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

result = binary_search(0, n - 1, target)
if result == None:
    print(None)
else:
    print(result + 1)
