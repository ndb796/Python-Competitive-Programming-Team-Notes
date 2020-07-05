import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

''' Dijkstra Shortest Path '''
def dijkstra(start):
    # Set the start node.
    q = [(0, start)]
    distance[start] = 0
    while q: # Until the queue is empty.
        # Pop the node who has the shortest path.
        dist, now = heapq.heappop(q)
        # If the node is already processed, pass.
        if distance[now] < dist:
            continue
        # Check the adjacent nodes of the current node.
        for i in graph[now]:
            cost = dist + i[1]
            # If the distance is shorter when going through the current node to the adjacent node.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# Run the Dijkstra algorithm.
dijkstra(start)

# Print all the shortest paths to all nodes.
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

'''
[Input Example 1]
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
[Output Example 1]
0
2
3
7
INFINITY
'''
