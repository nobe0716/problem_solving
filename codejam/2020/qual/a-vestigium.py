def solve(n, a):
    trace = sum(int(a[i][i]) for i in range(n))
    repeat_row, repeat_col = set(), set()
    row_set, col_set = [set() for _ in range(n)], [set() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            v = a[i][j]
            if v in row_set[i]:
                repeat_row.add(i)
            if v in col_set[j]:
                repeat_col.add(j)
            row_set[i].add(v)
            col_set[j].add(v)
    return ' '.join(map(str, [trace, len(repeat_row), len(repeat_col)]))


for t in range(1, int(input()) + 1):
    n = int(input())
    a = [input().split() for _ in range(n)]
    r = solve(n, a)
    print('Case #{}: {}'.format(t, r))
