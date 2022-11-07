import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque([])

for i in range(n):
    card.append(i+1)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())     # popleft하면서 바로 그 수 출력
    if len(card) == 1:
        break

print(*card)