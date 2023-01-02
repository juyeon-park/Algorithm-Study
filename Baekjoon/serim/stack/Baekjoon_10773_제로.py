import sys

k = int(sys.stdin.readline())
data = []

for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        data.pop()
    else:
        data.append(num)

print(sum(data))