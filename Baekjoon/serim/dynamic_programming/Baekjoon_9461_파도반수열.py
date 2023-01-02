<<<<<<< HEAD
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
=======
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
>>>>>>> 81c810962fd8e2745b26aa72cbbaad4642f7d3cf
