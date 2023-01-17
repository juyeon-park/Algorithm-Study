import sys

n = int(sys.stdin.readline())
house = list()

for i in range(n):
    # 집 번호 인덱스는 -1 해주기!!
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,n):
    # 리스트 전체를 다 바꿔줘야 다음 집의 경우의 수를 구할 수 있다.
    # 현재 집에 빨간색[][0]을 색칠할 경우, 전 집에서 초록색[][1]과 파란색[][2] 중 최솟값을 가져온다.
    house[i][0] = house[i][0] + min(house[i-1][1], house[i-1][2])
    # 현재 집에 초록색[][1]을 색칠할 경우, 전 집에서 빨간색[][0]과 파란색[][2] 중 최솟값을 가져온다.
    house[i][1] = house[i][1] + min(house[i-1][0], house[i-1][2])
    # 현재 집에 파란색[][2]을 색칠할 경우, 전 집에서 빨간색[][0]과 초록색[][1] 중 최솟값을 가져온다.
    house[i][2] = house[i][2] + min(house[i-1][0], house[i-1][1])

print(min(house[n-1]))