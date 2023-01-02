import sys

t = int(sys.stdin.readline())

for i in range(t):
    data = list(sys.stdin.readline())
    sum = 0
    for j in data:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            break

    if sum == 0:
        print("YES")
    else:
        print("NO")