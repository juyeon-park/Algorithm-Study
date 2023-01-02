import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start_node):
    visited[start_node] = 1
    for i in graph[start_node]:
        if visited[i] == 0:
            dfs(i)

visited = [0]*(n+1)
dfs(1)
print(sum(visited)-1)