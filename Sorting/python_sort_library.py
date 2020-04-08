n = 5

''' Python Sort Library (Basic) '''
data = [8, 5, 4, 7, 2]
data.sort()

for x in data:
    print(x)

print("---------------")

''' Python Sort Library (Based on a key) '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort(key=lambda x: x[0]) # Stable Sort (When using a key)

for x in data:
    print(x)

print("---------------")

''' Python Sort Library '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort() # Non-stable Sort (When not using a key)

for x in data:
    print(x)

print("---------------")
