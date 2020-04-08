n = 5
data = [8, 5, 4, 7, 2]

''' Counting Sort '''
# Initialize a list whose size is greater than a range of all values.
count = [0] * (max(data) + 1)

for i in range(n):
    count[data[i]] += 1 # Increase the value in the index.

for i in range(len(count)): # Check the sort information recorded on the list.
    for j in range(count[i]):
        print(i) # Print each index as many times as it appears.
