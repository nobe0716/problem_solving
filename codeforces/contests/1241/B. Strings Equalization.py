def is_possible(s, t):
    st = set(t)
    return any(e in st for e in set(s))


for _ in range(int(input())):
    s, t = input(), input()
    print('YES' if is_possible(s, t) else 'NO')
