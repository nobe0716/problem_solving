import heapq
import sys
from collections import defaultdict, deque


def solve(n, p, a):
    tree = defaultdict(set)
    a = [0] + a

    for i, j in enumerate(p, start=2):
        tree[i].add(j)
        tree[j].add(i)

    q = deque([1])
    while q:
        parent = q.popleft()
        for child in tree[parent]:
            q.append(child)
            tree[child].discard(parent)

    child_sum = list(a)
    child_cnt = [0] * (n + 1)
    tree_heap = defaultdict(list)

    def calc_child_sum(node):
        if not tree[node]:
            child_cnt[node] = 1
            return
        mul_complexity = 1
        for child in tree[node]:
            calc_child_sum(child)
            heapq.heappush(tree_heap[node], [-child_cnt[child], child])
            child_sum[node] += child_sum[child]
            child_cnt[node] += child_cnt[child]

    calc_child_sum(1)

    def proc(node, movers=0):
        if not tree[node]:
            return a[node] + movers

        num_of_citizen = child_sum[node] + movers
        optimal_spreads = num_of_citizen // len(tree[node])
        if num_of_citizen % len(tree[node]):
            optimal_spreads += 1

        exceed_cities = []
        for child in tree[node]:
            if child_sum[child] > optimal_spreads:
                exceed_cities.append((child_sum[child], child))

        if exceed_cities:
            exceed_cities.sort()
            return proc(exceed_cities[0][1])

        most_complex_child = tree_heap[node][0][1]
        return proc(most_complex_child, optimal_spreads - child_sum[most_complex_child])

    return proc(1)


# assert solve(3, [1, 1], [3, 1, 2]) == 3
# assert solve(3, [1, 1], [3, 1, 3]) == 4
# assert solve(5, [1, 1, 2, 2], [10, 3, 6, 1, 2]) == 6
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))

res = solve(n, p, a)
print(res)
