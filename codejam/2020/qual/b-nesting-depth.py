def solve(s):
    current_depth = 0
    r = ''
    for e in s:
        expected_level = int(e)
        if current_depth < expected_level:
            r += '(' * (expected_level - current_depth)
        elif current_depth > expected_level:
            r += ')' * (current_depth - expected_level)
        r += e
        current_depth = expected_level
    r += ')' * current_depth
    return r


for t in range(1, int(input()) + 1):
    s = input()
    r = solve(s)
    print('Case #{}: {}'.format(t, r))
