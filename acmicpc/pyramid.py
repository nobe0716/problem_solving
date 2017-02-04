class Solution:
    def distance(self, begin, end):
        # find array boundary
        max_value = max([begin, end])
        n = 1
        while n * (n + 1) / 2 <= max_value:
            n += 1
        n += 1
        map = [[0] * n for _ in range(n)]

        # draw traigle on circle
        c = 1
        for d in range(1, n):
            i = d
            j = 1
            for k in range(d):
                map[i][j] = c
                i -= 1
                j += 1
                c += 1

        # find position of given numbers
        begin_pos = None
        end_pos = None
        for i in range(n):
            for j in range(n):
                if map[i][j] == begin:
                    begin_pos = [i, j]
                if map[i][j] == end:
                    end_pos = [i, j]

        # answer will be vector distance between two position
        return abs(begin_pos[0] - end_pos[0]) + abs(begin_pos[1] - end_pos[1])

s = Solution()
print(s.distance(100, 1000))
print(s.distance(2, 3))
print(s.distance(6, 12))
assert(1 == s.distance(5, 2))
assert(0 == s.distance(7, 7))
assert(31 == s.distance(100, 1000))