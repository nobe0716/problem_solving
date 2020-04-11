t, b = list(map(int, input().split()))

"""
00101011110100110010
00101011010000110010.
"""


class QueryMgr:
    def __init__(self):
        self.turn = 0

    def query(self, idx):
        print(idx + 1, flush=True)
        self.turn += 1
        return int(input())


for _ in range(t):
    query_mgr = QueryMgr()
    a = [None] * b
    equal_pairs = []
    different_pairs = []

    none_idx = 0
    while True:
        for pairs in [equal_pairs, different_pairs]:
            if not pairs:
                continue
            first_pair = pairs[0]
            new_elem = query_mgr.query(first_pair[0])
            if a[first_pair[0]] != new_elem:
                for i, j in pairs:
                    a[i], a[j] = 1 - a[i], 1 - a[j]

        if query_mgr.turn % 2 == 1:  # do-dummy-query
            query_mgr.query(0)

        for i in range(query_mgr.turn % 10, 10, 2):
            if a[none_idx]:
                break
            sym_idx = b - none_idx - 1
            a[none_idx] = query_mgr.query(none_idx)
            a[sym_idx] = query_mgr.query(sym_idx)

            if a[none_idx] == a[sym_idx]:
                equal_pairs.append((none_idx, sym_idx))
            else:
                different_pairs.append((none_idx, sym_idx))
            none_idx += 1
        if a[none_idx] is not None and query_mgr.turn % 10 != 1:
            break
    print(''.join(map(str, a)), flush=True)
    r = input()
    if r == 'N':
        exit(-1)
