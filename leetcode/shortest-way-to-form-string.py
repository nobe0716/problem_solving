# 2022-07-16T20:51:20Z
from bisect import bisect
from collections import defaultdict


class Solution:
    # simplest - 3min
    def shortestWay(self, source: str, target: str) -> int:
        if set(target).difference(set(source)):
            return -1
        j = 0
        n = len(target)
        c = 0
        while j < n:
            for i, e in enumerate(source):
                if j < n and e == target[j]:
                    j += 1
            c += 1
        return c

    # 2022-07-16T20:57:01Z
    # complex - binary search - 5min
    def shortestWayBinarySearch(self, source: str, target: str) -> int:
        if set(target).difference(set(source)):
            return -1
        pos = defaultdict(list)
        for i, e in enumerate(source):
            pos[e].append(i)

        i = -1
        c = 1
        for j, e in enumerate(target):
            ni = bisect(pos[e], i)
            if ni >= len(pos[e]):
                i = pos[e][0]
                c += 1
            else:
                i = pos[e][ni]
        return c
