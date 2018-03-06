import sys

sys.setrecursionlimit = 20

class Solution(object):
    def back(self, N, d, idx, used):
        if idx == N + 1:
            return 1
        c = 0
        for candidate in d[idx]:
            if candidate in used:
                continue
            used.add(candidate)
            c += self.back(N, d, idx + 1, used)
            used.remove(candidate)
        return c

    def countArrangement(self, N):
        d = {}
        for i in range(1, N + 1):
            d[i] = []
            for j in range(1, N + 1):
                if i % j == 0 or j % i == 0:
                    d[i].append(j)
        return self.back(N, d, 1, set())