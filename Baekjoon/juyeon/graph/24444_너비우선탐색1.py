N, M, R = map(int, input().split())

# 그래프를 파이썬 딕셔너리로 구현해서 푸니 백준에서 정답은 맞지만 시간초과가 뜸
graph = dict()
for i in range(M):
    a, b = list(map(int, input().split()))
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


def bfs(graph, R, visited):
    need_visit = list()
    need_visit.append(R)
    visited[R] = 1
    count = 2

    while need_visit:
        node = need_visit.pop(0)
        for i in graph[node]:
            if visited[i] == 0:
                need_visit.append(i)
                visited[i] = count
                count += 1


visited = [0]*(N+1)
bfs(graph, R, visited)

for i in visited[1::]:
    print(i)
