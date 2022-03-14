# 2022-03-12 16:48:29.943087
# https://codeforces.com/problemset/problem/546/D
# Timeout but IO matters
# !/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def main():
    maximum_value_a = 5000001
    # maximum_value_a = 10

    LIMIT = 2235
    factors = [None] * maximum_value_a
    for i in range(4, maximum_value_a, 2):
        factors[i] = 2
    for i in range(2, LIMIT):
        if factors[i]:
            continue
        for j in range(i * 3, maximum_value_a, i * 2):
            if factors[j] is None:
                factors[j] = i

    t = [1] * maximum_value_a
    t[0] = 0

    for i in range(4, maximum_value_a):
        if factors[i]:
            t[i] = t[i // factors[i]] + 1

    for i in range(2, maximum_value_a):
        t[i] = t[i - 1] + t[i]

    def proc(a, b):
        return t[a] - t[b]

    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(proc(a, b))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
