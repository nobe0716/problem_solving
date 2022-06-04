# 2022-06-04T08:16:23Z

"""
Input
The first line contains two integers a and b, the two integers as described above (1 ≤ a, b ≤ 109). The second line contains one integer n, the number of queries (1 ≤ n ≤ 104). Then n lines follow, each line contains one query consisting of two integers, low and high (1 ≤ low ≤ high ≤ 109).

Output
Print n lines. The i-th of them should contain the result of the i-th query in the input. If there is no common divisor in the given range for any query, you should print -1 as a result for this query.


"""
import math
import bisect


def proc():
    def factorize(g):
        f = set()
        for i in range(1, int(math.ceil(math.sqrt(g))) + 1):
            if g % i == 0:
                f.add(i)
                f.add(g // i)

        return sorted(f)

    def exist(m):
        bisect.bisect_right(f, m)
        return False

    g = math.gcd(a, b)
    f = list(reversed(factorize(g)))

    res = []
    for low, high in q:
        ans = -1
        for e in f:
            if low <= e <= high:
                ans = e
                break
        res.append(ans)
    return res


a, b = map(int, input().split())
n = int(input())
q = []
for _ in range(n):
    low, high = map(int, input().split())
    q.append((low, high))

ans = proc()
for v in ans:
    print(v)
