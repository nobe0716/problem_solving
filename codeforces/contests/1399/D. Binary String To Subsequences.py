# https://codeforces.com/contest/1399/problem/D


def solve(n, s):
    groups = {'0': [], '1': []}
    group_info = [-1] * n

    group_info[0] = 1
    groups[s[0]].append(1)
    group_count = 1

    for i, e in enumerate(s[1:], start=1):
        if e == '1':
            if not groups['0']:
                group_count += 1
                group_no = group_count
            else:
                group_no = groups['0'].pop()
            groups['1'].append(group_no)
        else:
            if not groups['1']:
                group_count += 1
                group_no = group_count
            else:
                group_no = groups['1'].pop()
            groups['0'].append(group_no)
        group_info[i] = group_no
    return group_count, group_info


for _ in range(int(input())):
    n = int(input())
    s = input()
    r = solve(n, s)

    print(r[0])
    print(' '.join(map(str, r[1])))
