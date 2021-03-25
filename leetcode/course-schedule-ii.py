from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_to_next = defaultdict(set)
        next_to_pre = defaultdict(set)

        candidates = set(range(numCourses))
        for ai, bi in prerequisites:
            pre_to_next[bi].add(ai)
            next_to_pre[ai].add(bi)

            candidates.discard(ai)

        course_order = list(candidates)
        q = candidates
        while q:
            nq = set()
            for e in q:
                for next in pre_to_next[e]:
                    next_to_pre[next].discard(e)
                    if len(next_to_pre[next]) == 0:
                        course_order.append(next)
                        nq.add(next)

            q = nq

        if len(course_order) == numCourses:
            return course_order
        return []


s = Solution()
print(s.findOrder(numCourses=2, prerequisites=[[1, 0]]))
print(s.findOrder(numCourses=1, prerequisites=[]))
