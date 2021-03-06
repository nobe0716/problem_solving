from collections import defaultdict

from sortedcontainers import SortedDict


class TimeMap:

    def __init__(self):
        self.entries = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.entries[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.entries:
            return ''
        d = self.entries[key]
        idx = d.bisect_right(timestamp)
        if idx == 0:
            return ''
        return d[d.keys()[idx - 1]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
