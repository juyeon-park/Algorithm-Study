import sys

n = int(sys.stdin.readline())
wine = list()
for i in range(n):
    wine.append(int(sys.stdin.readline()))

dp = [0]
#잔이 1개만 있을 경우
dp.append(wine[0])
#잔이 2개만 있을 경우
if n > 1:
    dp.append(wine[0] + wine[1])
#잔이 3개 이상
for i in range(3, n+1):
    # wine은 인덱스 0부터 첫번째잔이라 인덱스 자체는 i-1이 기본이다
    # 이번 포도주를 마시고 앞 포도주를 마시지 않은 경우 :: k, k-2번째를 마신 경우
    case1 = wine[i-1] + dp[i-2]
    # 이번 포도주와 앞 포도주를 마신 경우 :: k, k-1번째를 마신 경우
    case2 = wine[i-1] + wine[i-2] + dp[i-3]
    # 이번 포도주를 마시지 않고 앞과 그 앞 포도주만 마신 경우 :: k-1, k-2번째를 마신 경우
    case3 = dp[i-1]
    # 세 개의 경우의 수 중에서 가장 큰 수를 dp에 넣는다.
    dp.append(max(case1, case2, case3))

print(dp[n])