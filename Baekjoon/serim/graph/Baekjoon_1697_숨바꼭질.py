import sys

n, k = map(int, sys.stdin.readline().split())
max = 100001
array = [0] * max


def bfs(V):
    need_visit = list()
    need_visit.append(V)
    while need_visit:
        node = need_visit.pop(0)
        if node == k:
            return array[node]
        for next in (node-1, node+1, node*2):
            if 0 <= next < max and not array[next]:
                array[next] = array[node]+1
                need_visit.append(next)


print(bfs(n))