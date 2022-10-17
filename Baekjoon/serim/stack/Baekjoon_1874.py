import sys

n = int(sys.stdin.readline())
cnt = 0
data = []
se = []

for i in range(0,n) :
    a = int(sys.stdin.readline())

    # a까지 data쌓기. cnt만큼 +입력하기, 마지막에 pop하면서 -입력해주기
    for i in range(cnt):
        cnt+=1
        data.append(cnt)
        print("+")

        if cnt==a:
            data.pop()
            print("-")



#미완