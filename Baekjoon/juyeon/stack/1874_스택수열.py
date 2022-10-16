import sys
isSequence = True
n = int(sys.stdin.readline())
count = 1
stack = []
answer = []
for i in range(n):
    m = int(sys.stdin.readline())
    while count < m+1:
        stack.append(count)
        answer.append('+')
        count += 1

    if stack[-1] == m:
        stack.pop()
        answer.append('-')
    else:
        isSequence = False
        break

if isSequence == False:
    print("NO")
else:
    for x in answer:
        print(x)
