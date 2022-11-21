# N = int(input())
# distance = list(map(int, input().split()))
# price = list(map(int, input().split()))
# price.pop()
# ans = 0
# while len(distance) > 0:
#     if price[0] == min(price):
#         ans += price[0] * sum(distance)
#         break
#     else:
#         ans = ans + price[0] * distance[0]
#         distance.pop(0)
#         price.pop(0)
# print(ans)


N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()
ans = 0
min_price = price[0]

for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
    ans += min_price * distance[i]
print(ans)
