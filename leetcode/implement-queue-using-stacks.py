class MyQueue(object):

    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        buf = []
        while len(self.s) > 0:
            buf.append(self.s.pop())
        v = buf.pop()
        while len(buf) > 0:
            self.s.append(buf.pop())
        return v

    def peek(self):
        buf = []
        while len(self.s) > 0:
            buf.append(self.s.pop())
        v = buf.pop()
        buf.append(v)
        while len(buf) > 0:
            self.s.append(buf.pop())
        return v

    def empty(self):
        return len(self.s) == 0


q = MyQueue()
q.push(1)
q.push(2)
print q.peek()
print q.peek()
