import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

A.sort()


def binary_search(value, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if A[mid] > value:
        return binary_search(value, start, mid-1)
    elif A[mid] < value:
        return binary_search(value, mid+1, end)
    else:
        return 1


for i in X:
    start = 0
    end = len(A)-1
    print(binary_search(i, start, end))
