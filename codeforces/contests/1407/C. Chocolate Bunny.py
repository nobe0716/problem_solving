# https://codeforces.com/contest/1407/problem/C
import functools

n = int(input())


@functools.lru_cache(None)
def get_mod(i: int, j: int):
    print('? {} {}'.format(i, j))
    r = int(input())
    return r


a = [None] * (n + 1)
mi = 1
for i in range(2, n + 1):
    m_mod_i = get_mod(mi, i)
    i_mod_m = get_mod(i, mi)

    if m_mod_i > i_mod_m:
        a[mi] = m_mod_i
        mi = i
    else:
        a[i] = i_mod_m

a[mi] = n

print('! {}'.format(' '.join(map(str, a[1:n + 1]))))
