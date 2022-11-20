import sys

n, k = map(int, sys.stdin.readline().split())
li = list()
for i in range(n):
    li.append(int(sys.stdin.readline()))
num = 0

while k > 0 :
    for i in range(n-1, -1, -1):
        num += int(k / li[i])
        k = k % li[i]
    if k == 0:
        break

print(num)
