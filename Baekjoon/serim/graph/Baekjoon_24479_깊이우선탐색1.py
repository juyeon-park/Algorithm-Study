import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드
n, m, r = map(int, sys.stdin.readline().split())
# 연결노드 그래프 초기화( 1번노드와 인덱스 값이 같게 하기 위해서 n+1로 )
# [[],[],[],[],[],[]]
graph = [[] for _ in range(n + 1)]
visted = [0] * (n + 1)
cnt = 1

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort()

def dfs(graph, v, visted):
    global cnt
    visted[v] = cnt
    for i in graph[v]:
        if visted[i] == 0:
            cnt += 1
            dfs(graph, i, visted)

dfs(graph, r, visted)

for i in range(n + 1):
    if i != 0:
        print(visted[i])