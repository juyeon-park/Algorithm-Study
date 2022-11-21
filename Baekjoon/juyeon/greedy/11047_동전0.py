N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)
count = 0
for i in coin:
    count += K // i
    K %= i

print(count)
