import sys

isSequence = True               #수열이 되는지 아닌지 판단
n = int(sys.stdin.readline())
count = 1
stack = []                      #수열이 적힐 공간
answer = []                     #+와 -가 적힐 공간

for i in range(n):
    m = int(sys.stdin.readline())
    while count < m+1:          #count가 1부터 시작해서 m+1까지 진행되어야함
        stack.append(count)     #count가 m까지는 계속해서 push이다.
        answer.append('+')
        count += 1

    if stack[-1] == m:          #만약 stack의 가장 마지막 부분이 m이면 pop해줌과 동시에 -를 입력해줘야한다.
        stack.pop()
        answer.append('-')
    else:
        isSequence = False      #stack의 마지막 부분이 m이 아니라면 수열이 될 수 없다. False처리
        break

if not isSequence:
    print("NO")
else:
    for x in answer:
        print(x)