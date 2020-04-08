n = 5
data = [8, 5, 4, 7, 2]

''' Quick Sort '''
def quick_sort(start, end):
    if start >= end: # If the subarray size is 1, exit the function.
        return
    pivot = start # The pivot is the first element of the subarray.
    left = start + 1
    right = end
    while left <= right:
        # Until finding an element bigger than the pivot,
        while left <= end and data[left] <= data[pivot]:
            left += 1
        # Until finding an element smaller than the pivot,
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right: # If two elements miss each other,
            data[right], data[pivot] = data[pivot], data[right]
        else: # If two elements don't miss each other,
            data[left], data[right] = data[right], data[left]
    # Sort the left part and right part respectively.
    quick_sort(start, right - 1)
    quick_sort(right + 1, end)

quick_sort(0, n - 1)

for x in data:
    print(x)
