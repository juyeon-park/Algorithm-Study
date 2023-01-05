n = int(input())
wine = list()
for _ in range(n):
    x = int(input())
    wine.append(x)

dp = [0]  # 최대로 먹을 수 있는 포도주의 양을 담는 리스트
dp.append(wine[0])  # 첫잔
if (n > 1):
    dp.append(wine[0] + wine[1])  # 두번째잔까지 먹을경우 최대 포도주 양

for i in range(3, n + 1):
    # wine(리스트) 0부터 시작하므로 i - 1
    # case1 : 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
    case1 = wine[i - 1] + dp[i - 2]
    # case2 : 이번 포도주를 먹고 이전 포도주도 먹은 경우
    case2 = wine[i - 1] + wine[i - 2] + dp[i - 3]
    # case3 : 이번 포도주를 먹지 않아야 하는 경우
    case3 = dp[i - 1]
    max_value = max(case1, case2, case3)

    dp.append(max_value)

print(dp[n])
