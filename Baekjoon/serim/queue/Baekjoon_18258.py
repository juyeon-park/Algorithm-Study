import sys
from collections import deque

n = int(sys.stdin.readline())
data = deque([])

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        data.append(a[1])
    elif a[0] == "pop":
        if len(data) == 0:
            print("-1")
        else:
            print(data.popleft())
    elif a[0] == "size":
        print(len(data))
    elif a[0] == "empty":
        if len(data) == 0:
            print("1")
        else:
            print("0")
    elif a[0] == "front":
        if len(data) == 0:
            print("-1")
        else:
            print(data[0])
    elif a[0] == "back":
        if len(data) == 0:
            print("-1")
        else:
            print(data[-1])
