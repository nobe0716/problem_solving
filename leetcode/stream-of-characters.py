from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.halt = False

    def add(self, word):
        if word:
            self.dict[word[0]].add(word[1:])
        else:
            self.halt = True

    def exists(self, word):
        if word:
            return self.dict[word[0]].exists(word[1:]) if word[0] in self.dict else False
        else:
            return True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie_head = TrieNode()
        self.trie_nodes = []
        for word in words:
            self.trie_head.add(word)

    def query(self, letter: str) -> bool:
        new_trie_nodes = []
        for trie_node in self.trie_nodes:
            if letter in trie_node.dict:
                new_trie_nodes.append(trie_node.dict[letter])
        self.trie_nodes = new_trie_nodes
        if letter in self.trie_head.dict:
            trie_node = self.trie_head.dict[letter]
            self.trie_nodes.append(trie_node)
        return any(trie_node.halt for trie_node in self.trie_nodes)


def test(procedures, inputs, expectations):
    s = StreamChecker(inputs[0][0])
    for input, expected in zip(inputs[1:], expectations[1:]):
        res = s.query(input[0])
        print(input, res, expected)
        assert res == expected


test(
    ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query",
     "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query",
     "query", "query", "query", "query", "query", "query", "query"],
    [[["ab", "ba", "aaab", "abab", "baa"]], ["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["a"], ["b"], ["b"],
     ["b"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"], ["b"], ["a"], ["a"], ["a"], ["b"],
     ["a"], ["a"], ["a"]],
    [None, False, False, False, False, False, True, True, True, True, True, False, False, True, True, True, True, False,
     False, False, True, True, True, True, True, True, False, True, True, True, False])
