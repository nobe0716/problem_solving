for i in xrange(int(raw_input())):
    n = int(raw_input())
    three_pots = (n-1) // 3
    fire_pots = (n-1) // 5
    fifteen_pots = (n-1) // 15
    sol = three_pots * (three_pots + 1) // 2 * 3 + fire_pots * (fire_pots + 1) // 2 * 5 - fifteen_pots * (fifteen_pots + 1) // 2 * 15
    print sol