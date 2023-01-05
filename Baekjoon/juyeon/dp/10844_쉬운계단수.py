import sys

N = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(N+1)]

# N=1 경우 초기화
for i in range(1,10): 
    dp[1][i] = 1

# N>=2 경우
for i in range(2,N+1):
    for j in range(10):
        # case1: 맨뒷자리수가 0인 경우
        if(j == 0):
            dp[i][j]= dp[i-1][1]

        # case2: 맨뒷자리수가 1~8인 경우
        elif(1<=j<=8):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
        # case3: 맨뒷자리수가 9인 경우
        else:
            dp[i][j]= dp[i-1][8]

print(sum(dp[N]) % 1000000000)