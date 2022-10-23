while True:
    n = input()
    stack = []
    if n == '.':
        break
    else:
        for i in n:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')' and len(stack) == 0:
                stack.append(i)
            elif i == ']' and len(stack) == 0:
                stack.append(i)
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()

        if len(stack) == 0:
            print('yes')
        else:
            print('no')
