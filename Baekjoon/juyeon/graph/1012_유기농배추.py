import sys
T = int(sys.stdin.readline())
sys.setrecursionlimit(10000)  # 재귀 깊이의 한계를 높게 설정해야함


def dfs(x, y):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= M:  # 상하좌우 배열의 범위가 2차원배열 안에 없을 경우 반복문을 빠져나옴
            continue
        if cabbage[nx][ny] == 1:
            cabbage[nx][ny] = 0  # 상하좌우로 인접한 값이 1인 땅을 0으로(방문했다는 의미로)
            dfs(nx, ny)


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbage = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())  # y = 가로, x = 세로
        cabbage[x][y] = 1

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:  # 배추 위치에 값이 1일때 dfs 실행
                dfs(i, j)
                cnt += 1
    print(cnt)
