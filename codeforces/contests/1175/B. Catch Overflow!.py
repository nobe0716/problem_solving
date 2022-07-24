_LIMIT = 2 ** 32


def proc():
    l = int(input())

    s = []
    value = 0
    loop_count = 1
    for _ in range(l):
        cmd = input()
        if cmd == 'add':
            value += 1
        elif cmd[0] == 'f':
            s.append((value, loop_count))
            value = 0
            loop_count = int(cmd.split()[1])
        else:  # end
            pv, pl = s.pop()
            value = pv + value * loop_count
            loop_count = pl

        if value >= _LIMIT:
            return 'OVERFLOW!!!'
    return value


print(proc())
