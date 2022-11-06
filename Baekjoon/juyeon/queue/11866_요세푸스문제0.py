from collections import deque
N, K = map(int, input().split())

li = deque([i for i in range(1, N+1)])
print('<', end="")
while len(li) > 0:
    for i in range(K-1):
        li.append(li[0])
        li.popleft()
    print(li.popleft(), end='')
    if len(li) > 0:
        print(', ', end='')
print('>')
