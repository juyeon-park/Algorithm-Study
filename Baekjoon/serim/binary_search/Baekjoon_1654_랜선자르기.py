import sys

k, n = map(int, sys.stdin.readline().split())
k_lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(k_lan)  # 랜선의 길이가 가장 짧은 것과 긴것을 start와 end로 둔다.

while start <= end:
    mid = (start + end) // 2    # mid 값 설정
    n_lan = 0   # 만들어지는 랜선의 갯수
    for i in k_lan:
        n_lan += i // mid   # 만들어지는 랜선의 갯수

    # 랜선의 갯수가 n개를 기준으로 많거나 적으면 시작이나 끝을 바꾸어 다시 계산한다.
    # 반복하다보면 start와 end의 값이 같아지는 경우가 나온다. 그 값이 최대 길이의 값이다.
    # start == end 일 때 while문 종료
    if n_lan >= n:
        start = mid + 1
    else :
        end = mid -1

print(end)