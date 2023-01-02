<<<<<<< HEAD
import sys

n = int(sys.stdin.readline())

dp = [0]*1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])
=======
import sys

n = int(sys.stdin.readline())

dp = [0]*1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])
>>>>>>> 81c810962fd8e2745b26aa72cbbaad4642f7d3cf
