def proc(s):
    stack = []
    for e in s:
        if not stack:
            stack.append(e)
        elif stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)
    return len(stack) == 0


s = input()
print('Yes' if proc(s) else 'No')
