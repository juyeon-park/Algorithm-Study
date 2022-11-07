import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
data = deque([])
sec = []

for i in range(n):
    data.append(i+1)

while True:
    for _ in range(k-1):        #인덱스는 0부터 시작이므로
        data.append(data.popleft()) # 인덱스 k-1번째의 데이터를 먼저 뺀 후, 맨 앞에 넣어준다.
    sec.append(data.popleft())      # data 덱에 있는 맨 앞의 값을 sec 덱에 넣어준다.
    if len(data) == 0:
        break

print(str(sec).replace('[', '<').replace(']', '>'))
    # 이렇게 쓰는건 그렇게 좋지는 않다. replace, f string 함수 등 쓸 거는 많다.