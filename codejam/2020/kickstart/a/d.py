# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
import sys
from collections import defaultdict

sys.setrecursionlimit(10000000)

Trie = lambda: [defaultdict(Trie), 0]


def add(head: Trie, str: str) -> None:
    node = head
    for i, e in enumerate(str):
        node = node[0][e]
        node[1] += 1


def solve(n, k, words):
    def traverse(node: Trie, level: int):
        total_number_of_words = 0
        total_score = 0
        for key in node[0].keys():
            count, score = traverse(node[0][key], level + 1)
            total_number_of_words += count
            total_score += score

        current_level_bundle_count = (node[1] - total_number_of_words) // k
        total_number_of_words += (current_level_bundle_count * k)
        total_score += (level * current_level_bundle_count)
        return total_number_of_words, total_score

    head = Trie()
    for w in words:
        add(head, w)
    return traverse(head, 0)


for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    words = [input() for _ in range(n)]
    r = solve(n, k, words)[1]
    print('Case #{}: {}'.format(t, r))
