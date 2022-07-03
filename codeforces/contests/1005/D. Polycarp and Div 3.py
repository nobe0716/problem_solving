# 2022-07-03T17:58:05Z

def proc(s):
    v = 0
    r = 0
    for e in s:
        e = int(e)
        v = v * 10 + e
        if v % 3 == 0 or (v % 10) % 3 == 0 or (v % 100) % 3 == 0 or (v % 1000) % 3 == 0:
            r += 1
            v = 0

    return r


s = input()
print(proc(s))
