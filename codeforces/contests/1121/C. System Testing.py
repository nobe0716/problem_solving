"""
wip
"""
import math


class Task:
    def __init__(self):
        self.current = 0
        self.total = 0
        self.interesting = False
        self.finished = False


n, k = map(int, input().split())
a = list(map(int, input().split()))
tasks = []

for e in a:
    task = Task()
    task.total = e
    tasks.append(task)

p = k
d = 0
finished_count = 0
while any(not t.finished for t in tasks):
    for i in range(p):
        if tasks[i].finished:
            continue
        tasks[i].current += 1
        if tasks[i].current == tasks[i].total:
            p = min(p + 1, n)
            tasks[i].finished = True
            finished_count += 1
            percent = math.floor(100.0 * finished_count / n + 0.5)
            for task in tasks[:p]:
                if task.finished or task.interesting:
                    continue
                if task.current == percent:
                    task.interesting = True

c = 0
for task in tasks:
    if task.interesting:
        c += 1
print(c)
