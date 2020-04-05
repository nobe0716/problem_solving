from operator import itemgetter


def solve(n, s):
    s = enumerate(s)
    s = sorted(s, key=itemgetter(1))
    schedule = [None] * n
    end_time = [0, 0]
    for idx, time in s:
        begin, end = time
        if begin < end_time[0] and begin < end_time[1]:
            return "IMPOSSIBLE"
        if begin >= end_time[0]:
            end_time[0] = end
            schedule[idx] = 'C'
        elif begin >= end_time[1]:
            end_time[1] = end
            schedule[idx] = 'J'
    return ''.join(schedule)


for t in range(1, int(input()) + 1):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    r = solve(n, s)
    print('Case #{}: {}'.format(t, r))
