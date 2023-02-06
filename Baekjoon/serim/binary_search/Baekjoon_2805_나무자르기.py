import sys

n, m = map(int, sys.stdin.readline().split())
hei = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(hei)

while start <= end:
    mid = (start + end) // 2
    cut = 0

    #i가 mid보다 클 때만 i에서 mid를 빼준 남은 값을 cut에 넣는다.
    for i in hei:
        if i > mid:
            cut += i - mid      # (i - mid) 라고 했더니 시간초과... 괄호가 문제가 있는걸까...

    # 나무 도막의 길이가 m보다 크거나 작아지면 다시 재야하기 때문에 start나 end를 다시 정해주고 이분탐색해야한다.
    # start와 end값이 같아지면 끝이난다.
    if cut >= m:
        start = mid + 1
    else :
        end = mid -1

print(end)