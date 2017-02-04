__author__ = 'sunghyo.jung'


for t in range(int(input())):
    n = int(input())

    path = {}
    ladders = {}
    snakes = {}
    distance = -1
    queue = list()
    visited = {}

    for i in range(n):
        f, t = map(int, input().split())
        ladders[f] = t
    n = int(input())
    for i in range(n):
        f, t = map(int, input().split())
        snakes[f] = t

    queue.append([1, 0])
    while len(queue) > 0:
        pos, weight = queue.pop(0)
        if pos == 100:
            distance = weight
            break
        for i in range(1, 7):
            new_pos = pos + i
            if new_pos in ladders:
                new_pos = ladders[new_pos]
            if new_pos in snakes:
                new_pos = snakes[new_pos]

            if new_pos not in visited:
                visited[new_pos] = True
                queue.append([new_pos, weight + 1])
    print(distance)
