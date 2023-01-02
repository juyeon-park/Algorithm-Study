import sys

t = int(sys.stdin.readline())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, len(dp)):
    dp[i] = dp[i-3] + dp[i-2]

for k in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])