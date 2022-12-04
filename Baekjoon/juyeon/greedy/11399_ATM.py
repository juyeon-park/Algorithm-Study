N = int(input())
num = list(map(int, input().split()))
time = []
num.sort()
x = 0
for i in num:
    x = x + i
    time.append(x)

print(sum(time))
