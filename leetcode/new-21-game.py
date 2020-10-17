class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or W == 0:
            return 1
        l = min(N + W, K + W)
        t = [1.0] + [0.0] * l

        acc_sum = 1.0
        for i in range(1, l):
            t[i] = acc_sum / W
            if i < K:
                acc_sum += t[i]
            if W <= i <= W + K:
                acc_sum -= t[i - W]

        return 1.0 - sum(t[N + 1:])


s = Solution()

epsilon_delta = 0.0001
assert abs(s.new21Game(0, 0, 2) - 1.0) < epsilon_delta
assert abs(s.new21Game(N=10, K=1, W=10) - 1.0) < epsilon_delta
assert abs(s.new21Game(N=1, K=1, W=3) - 0.3333) < epsilon_delta
assert abs(s.new21Game(N=21, K=17, W=10) - 0.73278) < epsilon_delta
assert abs(s.new21Game(N=6, K=1, W=10) - 0.6) < epsilon_delta
