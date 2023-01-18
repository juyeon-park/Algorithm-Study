import sys

n = int(sys.stdin.readline())

stair = list()
for i in range(n):
    stair.append(int(sys.stdin.readline()))

dp = list()

dp.append(stair[0])
if n > 1:
    dp.append(stair[0]+stair[1])
    if n > 2:
        dp.append(max(stair[0]+stair[2], stair[1]+stair[2]))

        for i in range(3, n): # 마지막 계단은 이미 밟은 상태 (무조건 밟아야함)
            # 전 계단을 밟은 경우 (전전 계단은 건너 뜀)
            case1 = dp[i-3]+stair[i-1]+stair[i]
            # 전 계단을 밟지 않고 전전 계단에서 건너 뛴 경우
            case2 = dp[i-2]+stair[i]
            # case1과 case2 중 최댓값을 dp에 넣음
            dp.append(max(case1, case2))

print(dp.pop())