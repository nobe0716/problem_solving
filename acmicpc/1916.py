n = int(input())
m = int(input())
MAXIMUM_VALUE = 100000000000
r = [MAXIMUM_VALUE] * (n + 1)
v = list(range(1, n + 1))

d = {}


def get_dist(a, b):
    return d[a][b] if (a in d and b in d[a]) else MAXIMUM_VALUE


def put_dist(a, b, c):
    if a not in d:
        d[a] = {}
    if b not in d[a] or d[a][b] > c:
        d[a][b] = c

for _ in range(m):
    a, b, c = map(int, input().split())
    put_dist(a, b, c)

# print(d)
begin, end = map(int, input().split())
r[begin] = 0

p = begin
v.remove(p)

for _ in range(n - 1):
    if p == end:
        break

    for i in v:
        dist = get_dist(p, i)
        if r[i] > r[p] + dist:
            r[i] = r[p] + dist
    min_dist = MAXIMUM_VALUE
    # print("p is " + str(p) + ' ' + str(v))
    # print(r)
    for i in v:
        if r[i] < min_dist:
            min_dist = r[i]
            p = i
    v.remove(p)
print(r[end])
