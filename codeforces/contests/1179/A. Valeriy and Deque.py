# 2022-06-05T11:44:52Z
from collections import deque


def proc(n, q, a, queries):
    dq = deque(a)
    ans = []
    pivot = None
    maxa = max(a)
    for i in range(3 * n):
        a, b = dq.popleft(), dq.popleft()
        if a > b:
            dq.appendleft(a)
            dq.append(b)
        else:
            dq.append(a)
            dq.appendleft(b)
        ans.append((a, b))
        if a == maxa and pivot is None:
            pivot = i

    res = []
    for e in queries:
        e -= 1

        if e <= pivot:
            res.append(ans[e])
        else:
            idx = pivot + (e - pivot) % (n - 1)
            res.append(ans[idx])

    return res


n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = []

for _ in range(q):
    x = int(input())
    queries.append(x)

ans = proc(n, q, a, queries)
for a, b in ans:
    print(a, b)
