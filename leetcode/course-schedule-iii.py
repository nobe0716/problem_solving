import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        c = 0
        q = []
        courses.sort(key=itemgetter(1, 0))
        for t, d in courses:
            c += t
            heapq.heappush(q, -t)

            if c > d:
                c += heapq.heappop(q)

        return len(q)


s = Solution()
assert s.scheduleCourse(courses=[[2, 10], [2, 19], [3, 19], [5, 15], [5, 16], [6, 7], [8, 14], [10, 11]]) == 5
assert s.scheduleCourse(courses=[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
assert s.scheduleCourse(courses=[[5, 5], [4, 6], [2, 6]]) == 2
