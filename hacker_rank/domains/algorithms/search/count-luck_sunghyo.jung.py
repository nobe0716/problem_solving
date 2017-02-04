__author__ = 'sunghyo.jung'

def get_wand(f, n, m):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    sp = []
    ep = []
    visited = [[False for i in range(m + 2)] for j in range(n + 2)]
    log = [[-1 for i in range(m + 2)] for j in range(n + 2)]
    count = [[0 for i in range(m + 2)] for j in range(n + 2)]
    queue = []

    for i in xrange(0, n + 2):
        for j in xrange(0, m + 2):
            if f[i][j] == 'M':
                sp = [i, j]
            if f[i][j] == '*':
                ep = [i, j]
            if f[i][j] == 'X':
                visited[i][j] = True

    visited[sp[0]][sp[1]] = True
    queue.append(sp)
    while len(queue) > 0:
        pos = queue.pop(0)
        if pos[0] == ep[0] and pos[1] == ep[1]:
            break
        for i in xrange(4):
            new_pos = [pos[0] + di[i], pos[1] + dj[i]]
            if not visited[new_pos[0]][new_pos[1]]:
                log[new_pos[0]][new_pos[1]] = i
                visited[new_pos[0]][new_pos[1]] = True
                queue.append(new_pos)
                count[pos[0]][pos[1]] += 1
    wand = 0
    current_idx = (log[ep[0]][ep[1]] + 2) % 4
    while sp[0] != ep[0] or sp[1] != ep[1]:
        idx = (log[ep[0]][ep[1]] + 2) % 4
        if current_idx != idx:
            current_idx = idx
        if count[ep[0]][ep[1]] > 1:
            wand += 1
        ep[0] += di[idx]
        ep[1] += dj[idx]
    if count[sp[0]][sp[1]] > 1:
        wand += 1
    return wand

for t in xrange(int(raw_input())):
    n, m = map(int, raw_input().split())
    f = list()
    f.append('X' * (m + 2))
    for i in xrange(n):
        f.append('X' + raw_input() + 'X')
    f.append('X' * (m + 2))
    k = int(raw_input())
    if k == get_wand(f, n, m):
        print 'Impressed'
    else:
        print 'Oops!'
