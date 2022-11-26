import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
num = 0

p.sort()        # 작은 수부터 정렬
for i in range(n):
    for j in range(i+1):
        num += p[j]

print(num)