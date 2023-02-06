import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()

def binary(li, b, start, end):  # 확인할 리스트, 비교할 수, start, end는 인덱스
    if start > end:
        return 0

    mid = (start + end) // 2

    if li[mid] == b:
        return 1
    if li[mid] > b:
        return binary(li, b, start, mid-1)
    if li[mid] < b:
        return binary(li, b, mid+1, end)

for i in b:
    print(binary(a, i, 0, n-1))