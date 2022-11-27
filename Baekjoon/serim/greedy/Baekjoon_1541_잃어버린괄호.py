import sys

a = sys.stdin.readline().split("-")
answer = []
for i in a:
    cnt = 0
    b = i.split("+")
    for j in b:
        cnt += int(j)
    answer.append(cnt)
number = answer[0]
for i in range(1, len(answer)):
    number -= answer[i]
print(number)