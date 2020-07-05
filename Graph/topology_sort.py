from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
   a, b = map(int, input().split())
   graph[a].append(b)
   indegree[b] += 1

''' Topology Sort '''
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()

'''
[Input Example 1]
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
[Output Example 1]
1 2 5 3 6 4 7
'''
