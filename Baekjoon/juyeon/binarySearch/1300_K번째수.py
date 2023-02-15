import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        ans = mid
        end = mid-1
    else:
        start = mid+1
print(ans)
