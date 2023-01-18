import sys
N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]

dp = [0] * N


if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0]+stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[2]+stairs[1])
    for i in range(3, N):
        dp[i] = max(stairs[i] + dp[i-2], stairs[i]+stairs[i-1]+dp[i-3])

print(dp[N-1])
