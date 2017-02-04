__author__ = 'sunghyo.jung'
for t in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    for e in a:
        for f in b:
            if e + f >= k:
                b.remove(f)
                break
    print("YES" if len(b) == 0 else "NO")