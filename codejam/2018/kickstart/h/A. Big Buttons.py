from collections import defaultdict


class Trie:
    def __init__(self):
        self.halt = False
        self.next = defaultdict(Trie)


def get_sum(current_prefix, current_sum, node):
    r = 0
    # if node.halt:
    #     r += current_sum
    if node.halt:
        # print('halt at ' + current_prefix)
        return 0
    for color in 'RB':
        if color not in node.next:
            # print('add at ' + current_prefix + color + '*', current_sum)
            r += current_sum
        else:
            r += get_sum(current_prefix + color, current_sum // 2, node.next[color])
    return r


for t in range(0, int(input())):
    head = Trie()
    n, p = map(int, input().split())
    for _ in range(p):
        prefix = input()
        node = head
        for c in prefix:
            node = node.next[c]
            node.v = c
        node.halt = True
    # v = 2 ** n
    res = get_sum('', 2 ** (n - 1), head)
    print('Case #{}: {}'.format(t + 1, res))
