class MyStack(object):
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        v = None
        buf = []
        while len(self.q) > 0:
            v = self.q.pop(0)
            if len(self.q) > 0:
                buf.append(v)
        self.q = buf
        return v

    def top(self):
        v = None
        buf = []
        while len(self.q) > 0:
            v = self.q.pop(0)
            buf.append(v)
        self.q = buf
        return v

    def empty(self):
        return len(self.q) == 0