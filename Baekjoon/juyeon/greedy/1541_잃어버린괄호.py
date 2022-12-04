N = input().split('-')
num = []


for i in N:
    sum = 0
    i = i.split('+')
    for j in i:
        sum = sum + int(j)
    num.append(sum)

ans = num[0]
for i in range(1, len(num)):
    ans = ans - num[i]
print(ans)
