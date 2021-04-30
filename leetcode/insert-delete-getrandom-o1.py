import random


class RandomizedSet:

    def __init__(self):
        self.pos = dict()
        self.keys = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.keys.append(val)
        self.pos[val] = len(self.keys) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        self.pos[self.keys[-1]] = idx
        self.keys[idx], self.keys[-1] = self.keys[-1], self.keys[idx]
        self.keys.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return self.keys[random.randint(0, len(self.keys) - 1)]
