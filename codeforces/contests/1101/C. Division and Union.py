def solve(n, lrs):
    elements = enumerate(lrs)
    elements = list(sorted(elements, key=lambda x: x[1][1]))

    i, j = 0, n - 1
    g_1 = elements[i][1]
    g_2 = elements[j][1]

    a_group_index = [elements[i][0]]
    b_group_index = [elements[j][0]]

    while len(a_group_index) + len(b_group_index) < n:
        while i + 1 != j and g_1[1] >= elements[i + 1][1][0]:
            i += 1
            a_group_index.append(elements[i][0])
            g_1[1] = max(g_1[1], elements[i][1][1])

        while j - 1 != i and g_2[0] <= elements[j - 1][1][1]:
            j -= 1
            b_group_index.append(elements[j][0])
            g_2[0] = min(g_2[0], elements[j][1][0])

        if len(a_group_index) + len(b_group_index) == n:
            break

        i += 1
        a_group_index.append(elements[i][0])
        g_1[1] = max(g_1[1], elements[i][1][1])

    if g_1[1] >= g_2[0]:
        return "-1"

    r = [0] * n
    for e in a_group_index:
        r[e] = 1
    for e in b_group_index:
        r[e] = 2
    return " ".join(map(str, r))


for _ in range(int(input())):
    n = int(input())
    lrs = [list(map(int, input().split())) for _ in range(n)]

    print(solve(n, lrs))
