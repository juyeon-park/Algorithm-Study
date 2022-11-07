import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        q.append(com[1])
    elif com[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if len(q) != 0:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif com[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
