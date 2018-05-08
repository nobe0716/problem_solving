class Solution(object):
    def countBits(self, num):
        return [len(list(filter(lambda x: x == '1', bin(n)))) for n in range(num + 1)]