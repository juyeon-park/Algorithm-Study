import sys

gas = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))
gasLiter = list(map(int, sys.stdin.readline().split()))

answer = 0
mincost = gasLiter[0]

for i in range(gas-1):
    if gasLiter[i] < mincost:
        mincost = gasLiter[i]
    answer += mincost * dis[i]

print(answer)