import sys
from collections import Counter

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

# Counter 사용하는 방법 => 딕셔너리 형태로 반환해줌
count_list = Counter(n)

for i in m:
    print(count_list[i], end=' ')


# 이분탐색으로 풀려고 했으나 시간초과 발생
# n.sort()
# def binary_search(value, start, end):
#     if start > end:
#         return 0

#     mid = (start + end) // 2
#     if n[mid] > value:
#         return binary_search(value, start, mid-1)
#     elif n[mid] < value:
#         return binary_search(value, mid+1, end)
#     else:
#         return n[start:end+1].count(value)

# for i in m:
#     start = 0
#     end = len(n)-1
#     print(binary_search(i, start, end), end=' ')
