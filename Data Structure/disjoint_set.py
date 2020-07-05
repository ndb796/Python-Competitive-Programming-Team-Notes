# Find the root node of x recursively.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union the two sets.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# Process union operations.
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('Root nodes for all nodes: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('Parent Table: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

'''
[Input Example 1]
6 4
1 4
2 3
2 4
5 6
[Output Example 1]
Root nodes for all nodes: 1 1 1 1 5 5 
Parent Table: 1 1 1 1 5 5
'''
