class Solution(object):
    def findMinArrowShots(self, points):
        if len(points) <= 1:
            return len(points)

        points = list(sorted(points, key=lambda p: p[1]))
        # print(points)
        r = float('-inf')
        c = 0
        for p in points:
            if p[0] > r:
                r = p[1]
                c += 1
        return c
