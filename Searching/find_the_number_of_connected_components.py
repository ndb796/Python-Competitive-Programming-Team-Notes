''' Find the number of connected components '''
from collections import deque

n = 15
m = 14
data = [
    '00000111100000',
    '11111101111110',
    '11011101101110',
    '11011101100000',
    '11011111111111',
    '11011111111100',
    '11000000011111',
    '01111111111111',
    '00000000011111',
    '01111111111000',
    '00011111111000',
    '00000001111000',
    '11111111110011',
    '11100011111111',
    '11100011111111'
]

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if data[x][y] == '0' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

result = 0
for i in range(n):
    for j in range(m):
        # Find the number of connected components consisting only of '0'.
        if data[i][j] == '0' and not visited[i][j]:
            bfs(i, j)
            result += 1

print(result)
