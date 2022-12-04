N = int(input())
time = []
for _ in range(N):
    a = list(map(int, input().split()))
    time.append(a)


time = sorted(time, key=lambda x: x[0])
time = sorted(time, key=lambda x: x[1])

cnt = 0
ltime = 0
for i, j in time:
    if i >= ltime:
        cnt += 1
        ltime = j
print(cnt)
