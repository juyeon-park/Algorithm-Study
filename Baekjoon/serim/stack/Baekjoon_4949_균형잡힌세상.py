import sys

while True:
    sen = sys.stdin.readline().rstrip()
    if sen == ".":
        break

    stack = []
    check = True

    for i in sen:
        if i == "(":
            stack.append(i)

        elif i == "[":
            stack.append(i)

        elif i == ")":
            if len(stack) == 0 or stack[-1] == "[":
                check = False
                break
            elif len(stack) != 0 and stack[-1] == "(":
                stack.pop()

        elif i == "]":
            if len(stack) == 0 or stack[-1] == "(":
                check = False
                break
            elif len(stack) != 0 and stack[-1] == "[":
                stack.pop()

    if check and len(stack) == 0:
        print("yes")
    else:
        print("no")