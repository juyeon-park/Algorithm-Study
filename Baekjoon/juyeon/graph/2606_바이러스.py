N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start_node):
    visited[start_node] = 1
    for i in graph[start_node]:
        if visited[i] == 0:
            dfs(i)


dfs(1)
print(sum(visited)-1)
