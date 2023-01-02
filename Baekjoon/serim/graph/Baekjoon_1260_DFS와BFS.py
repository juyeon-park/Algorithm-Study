import sys
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    edge = list(map(int, sys.stdin.readline().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for i in graph:
    i.sort()

dfs_visit = [False]*(n+1)

def dfs(V):
    dfs_visit[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not dfs_visit[i]:
            dfs(i)

def bfs(V):
    visited = list()
    need_visit = list()
    need_visit.append(V)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

dfs(v)
print()
bfs_visit = bfs(v)
for i in bfs_visit:
    print(i, end=' ')