import sys
T = int(sys.stdin.readline())
for _ in range(T):
    str = sys.stdin.readline()
    stack = []
    for i in str:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
