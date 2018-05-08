class Solution(object):
    def compareVersion(self, version1, version2):
        def cmp(a, b):
            if len(a) == len(b) == 0:
                return 0
            r, l = int(a[0]) if len(a) > 0 else 0, int(b[0]) if len(b) > 0 else 0
            if r > l:
                return 1
            if r < l:
                return -1
            return cmp(a[1:], b[1:])
        return cmp(version1.split('.'), version2.split('.'))
