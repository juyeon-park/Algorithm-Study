import sys
N = int(sys.stdin.readline())
home = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0]
    home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1]
    home[i][2] = min(home[i-1][0], home[i-1][1]) + home[i][2]
print(min(home[N-1]))
