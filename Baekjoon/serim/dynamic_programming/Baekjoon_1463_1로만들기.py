import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]    #인덱스와 수를 맞춰주기 위해 n+1 시작

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

#print(dp)
print(dp[n])