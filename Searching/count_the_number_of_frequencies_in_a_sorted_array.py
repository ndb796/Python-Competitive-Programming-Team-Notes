from bisect import bisect_left, bisect_right

# Count the number of frequencies of elements whose value is between [left, right] in a sorted array.
def count_the_number_of_frequencies_in_a_sorted_array(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9] 

# Count the number of frequencies of elements whose value is 4 in a sorted array.
print(count_the_number_of_frequencies_in_a_sorted_array(array, 4, 4))

# Count the number of frequencies of elements whose value is between [-1, 3] in a sorted array.
print(count_the_number_of_frequencies_in_a_sorted_array(array, -1, 3))
