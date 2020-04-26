''' Number of intersection points of two lines in 1 dimension '''
def num_of_intersect_two_lines(line_1, line_2):
    return max(min(line_1[1], line_2[1]) - max(line_1[0], line_2[0]) + 1, 0)

# Case 1
line_1 = [3, 7]
line_2 = [6, 9]

print(num_of_intersect_two_lines(line_1, line_2))

# Case 2
line_1 = [3, 5]
line_2 = [7, 9]

print(num_of_intersect_two_lines(line_1, line_2))
