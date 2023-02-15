import sys
N, C = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(N)]
x.sort()

start = 1
end = x[-1] - x[0]
ans = 0


while start <= end:
    mid = (start+end)//2
    print(mid)
    cnt = 1
    value = x[0]
    for i in range(1, len(x)):
        if x[i] >= value+mid:
            value = x[i]
            cnt += 1
    if cnt >= C:
        start = mid+1
        ans = mid
    else:
        end = mid - 1
print(ans)
