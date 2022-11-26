import sys

n = int(sys.stdin.readline())
info = []
for i in range(n):
    start,end = map(int, sys.stdin.readline().split())
    info.append([start, end])

info.sort(key = lambda x:x[0])
info.sort(key = lambda x:x[1])

last = 0
cnt = 0

for i, j in info:
    if i>= last:
        cnt += 1
        last = j

print(cnt)