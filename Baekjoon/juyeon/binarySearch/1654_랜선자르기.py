import sys
K, N = map(int, sys.stdin.readline().split())
num = [int(sys.stdin.readline()) for _ in range(K)]


def lan_len(value):  # 랜선 개수 구하는 함수
    cnt = 0
    for i in num:
        cnt += i // value
    return cnt


def binary_search(start, end):
    if start > end:
        return end
    mid = (start+end)//2
    mid_len = lan_len(mid)
    if mid_len < N:
        return binary_search(start, mid-1)
    elif mid_len >= N:
        return binary_search(mid+1, end)


print(binary_search(1, max(num)))
