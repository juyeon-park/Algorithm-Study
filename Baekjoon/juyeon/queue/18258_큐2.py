import sys
N = int(sys.stdin.readline())
queue = []
idx = 0
for _ in range(N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == idx:
            print(-1)
        else:
            print(queue[idx])
            idx += 1
    elif com[0] == 'size':
        print(len(queue)-idx)
    elif com[0] == 'empty':
        if len(queue) == idx:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == idx:
            print(-1)
        else:
            print(queue[idx])
    elif com[0] == 'back':
        if len(queue) == idx:
            print(-1)
        else:
            print(queue[-1])
