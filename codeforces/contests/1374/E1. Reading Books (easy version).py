from typing import List, Tuple


def solve(n: int, k: int, tab: List[Tuple[int, int, int]]):
    both, a_only, b_only = [], [], []
    for t, a, b in tab:
        if a == 1 and b == 1:
            both.append(t)
        elif a == 1:
            a_only.append(t)
        elif b == 1:
            b_only.append(t)
    both.sort()
    a_only.sort()
    b_only.sort()

    idx_both = idx_a_only = idx_b_only = 0
    len_both, len_a_only, len_b_only = len(both), len(a_only), len(b_only)
    times = []
    while len(times) < k and idx_both < len_both and idx_a_only < len_a_only and idx_b_only < len_b_only:
        if both[idx_both] < a_only[idx_a_only] + b_only[idx_b_only]:
            times.append(both[idx_both])
            idx_both += 1
        else:
            times.append(a_only[idx_a_only] + b_only[idx_b_only])
            idx_a_only += 1
            idx_b_only += 1
    while len(times) < k and idx_both < len_both:
        times.append(both[idx_both])
        idx_both += 1

    while len(times) < k and idx_a_only < len_a_only and idx_b_only < len_b_only:
        times.append(a_only[idx_a_only] + b_only[idx_b_only])
        idx_a_only += 1
        idx_b_only += 1
    return sum(times) if len(times) == k else -1


n, k = map(int, input().split())
tab = []
for _ in range(n):
    t, a, b = map(int, input().split())
    tab.append((t, a, b))
print(solve(n, k, tab))
