import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        data.append(a[1])
    elif a[0] == "pop":
        if len(data)==0:
            print("-1")
        else:
            print(data.pop()) #print안에 pop을 넣어도 실행됨
    elif a[0] == "size":
        print(len(data))
    elif a[0] == "empty":
        if len(data)==0:
            print("1")
        else:
            print("0")
    elif a[0] == "top":
        if len(data)==0:
            print("-1")
        else:
            print(data[-1]) #가장 마지막 순서의 배열은 -1로 표현 가능