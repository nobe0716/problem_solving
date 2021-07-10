# https://codeforces.com/contest/1400/problem/B
def solve(p, f, cnt_s, cnt_w, s, w):
    if s > w:
        cnt_s, cnt_w = cnt_w, cnt_s
        s, w = w, s

    r = 0
    for a in range(cnt_s + 1):
        if a * s > p:
            continue
        b = (p - a * s) // w
        b = min(b, cnt_w)

        c = min(f // s, cnt_s - a)
        d = (f - c * s) // w
        d = min(d, cnt_w - b)
        r = max(r, a + b + c + d)
    return r


for _ in range(int(input())):
    p, f = map(int, input().split())
    cnt_s, cnt_w = map(int, input().split())
    s, w = map(int, input().split())

    res = solve(p, f, cnt_s, cnt_w, s, w)
    print(res)
