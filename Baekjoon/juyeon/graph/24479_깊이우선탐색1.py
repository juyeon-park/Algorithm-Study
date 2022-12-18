import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려줌. 안해주면 RecursionError 발생
N, M, R = map(int, sys.stdin.readline().split())

# 그래프를 파이썬 딕셔너리로 구현해서 푸니 백준에서 정답은 맞지만 시간초과가 뜸
graph = dict()
for i in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]
for value in graph.values():
    value.sort()

# 그래프를 파이썬 리스트로 구현한 코드
# graph = [[] for _ in range(N+1)]
# for i in range(M):
#     edge = list(map(int,input().split()))
#     graph[edge[0]].append(edge[1])
#     graph[edge[1]].append(edge[0])
# for i in range(N+1):
#     graph[i].sort()

visited = [0]*(N+1)
count = 1


def dfs(graph, R, visited):
    global count
    visited[R] = count

    for i in graph[R]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)


dfs(graph, R, visited)

for i in visited[1::]:
    print(i)
