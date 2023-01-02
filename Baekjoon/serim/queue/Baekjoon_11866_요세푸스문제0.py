from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
data = deque([])

for i in range(n):
    data.append(i+1)

print("<", end="")
while data:
    for _ in range(k-1):        #인덱스가 0부터 시작하므로 k-1
        data.append(data[0])    #맨 처음 수를 맨 뒤에 삽입한다
        data.popleft()          #맨 뒤에 삽입했으니 앞을 지워준다.
    print(data.popleft(), end="")   #k-1번째 행위가 끝나면 data의 맨 앞의 데이터는 삽입없이 지워주며 바로 프린트한다. 이 행위 반복.
    if data:                    #데이터가 아직 남아있으므로, 이 행위를 반복한다.
        print(", ", end="")
print(">")