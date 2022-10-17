import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        stack.append(int(com[1]))
    elif com[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
