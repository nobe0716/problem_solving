s = input()
stack = []
c = 0

for e in s:
    if len(stack) == 0 or stack[-1] != e:
        stack.append(e)
    else:
        stack.pop()
        c += 1
print("NO" if c % 2 == 0 else "YES")
