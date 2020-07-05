''' Binary Search (Iterative Method) '''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # If the target is found, return the mid index.
        if array[mid] == target:
            return mid
        # If the value of the mid index is greater than the target, search the left part.
        elif array[mid] > target:
            end = mid - 1
        # If the value of the mid index is smaller than the target, search the right part.
        else:
            start = mid + 1
    return None

n = 10
target = 13
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n - 1)
if result == None:
    print(None)
else:
    print(result + 1)
