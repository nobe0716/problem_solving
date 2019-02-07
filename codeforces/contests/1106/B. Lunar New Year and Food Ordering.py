from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

pack = deque(sorted(enumerate(c), key=lambda x: x[1]))
# idx_for_food = {}
# for i in range(n):
#     idx_for_food[pack[i][0]] = i
# print(pack)
total_earned = 0
for _ in range(m):
    t, d = map(int, input().split())
    t -= 1  # for 0 base idx
    price = 0
    is_break = False

    if a[t] >= d:
        a[t] -= d
        price = c[t] * d
    else:
        d -= a[t]
        price = c[t] * a[t]
        a[t] = 0
        while d > 0:
            while len(pack) > 0 and a[pack[0][0]] == 0:
                pack.popleft()
            if len(pack) == 0:
                is_break = True
                break
            alternative_idx = pack[0][0]
            alternative_count = min(a[alternative_idx], d)
            d -= alternative_count
            a[alternative_idx] -= alternative_count
            price += (c[alternative_idx] * alternative_count)

    if not is_break:
        total_earned += price
        print(price)
    else:
        print(0)
#
# print(total_earned)
