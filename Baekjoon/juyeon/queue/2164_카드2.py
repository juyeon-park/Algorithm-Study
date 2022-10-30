from collections import deque

N = int(input())

# 아래 3줄을 더 짧게 q = deque([i for i in rannge(1,N+1)])로 표현 가능 =>리스트 내포
q = deque()
for i in range(1, N+1):
    q.append(i)

# for문 대신 while문을 쓰면 더 편함
for _ in range(N):
    if len(q) == 1:
        print(q[0])
        break
    else:
        q.popleft()
        q.append(q[0])
        q.popleft()
