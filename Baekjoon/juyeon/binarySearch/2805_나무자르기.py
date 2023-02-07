import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


def cutting(value):
    cnt = 0
    for i in tree:
        if i > value:
            cnt += i-value
    return cnt


def binary_search(start, end):
    if start > end:
        return end
    mid = (start+end)//2
    tree_length = cutting(mid)
    if tree_length >= M:
        return binary_search(mid+1, end)
    elif tree_length < M:
        return binary_search(start, mid-1)


print(binary_search(1, max(tree)-1))
