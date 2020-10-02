import bisect


class SnapshotArray:

    def __init__(self, length: int):
        # self.v = [0] * length
        self.last_snapshot_id = 0
        self.keys = [[0] for _ in range(length)]
        self.vals = [[0] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.keys[index][-1] == self.last_snapshot_id:  # value changed in same snapshot
            self.vals[index][-1] = val
        else:
            self.keys[index].append(self.last_snapshot_id)
            self.vals[index].append(val)

    def snap(self) -> int:
        self.last_snapshot_id += 1
        return self.last_snapshot_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pos = bisect.bisect(self.keys[index], snap_id)
        if pos == len(self.keys[index]):
            return self.vals[index][-1]
        elif self.keys[index][pos] == snap_id:
            return self.vals[index][pos]
        return self.vals[index][pos - 1]


# Your SnapshotArray object will be instantiated and called as such:
ops = ["SnapshotArray", "set", "snap", "set", "get"]
args = [[3], [0, 5], [], [0, 6], [0, 0]]
# length = 3

obj = SnapshotArray(args[0][0])
for op, arg in zip(ops[1:], args[1:]):
    if op == 'set':
        obj.set(*arg)
    elif op == 'snap':
        obj.snap()
    elif op == 'get':
        print(obj.get(*arg))
