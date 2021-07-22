# https://codeforces.com/problemset/problem/1395/C
n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

solution_set = {x & y for x in a for y in b}

for x in a[1:]:
    c = {x & y for y in b}
    solution_set = {x | y for x in solution_set for y in c}

print(min(solution_set))
