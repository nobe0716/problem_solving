class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        v = [g - c for g, c in zip(gas, cost)]
        s = 0
        mi, mv = None, float('inf')
        for i in range(n):
            s += v[i]
            if s < mv:
                mv, mi = s, i
        return (mi + 1) % n if s >= 0 else -1
