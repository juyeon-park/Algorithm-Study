import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    tmpL = list(map(int, sys.stdin.readline().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])

for i in range(n+1):
    graph[i].sort()

# BFS 함수
def bfs(graph, R, visited):
    queue = deque([R])
    visited[R] = 1
    count = 2
    while queue:
        R = queue.popleft()
        for i in graph[R]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = count
                count += 1

visited = [0] * (n + 1)
bfs(graph, r, visited)

for i in visited[1::]:
    print(i)