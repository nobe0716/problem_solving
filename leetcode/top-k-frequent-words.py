from collections import defaultdict
import heapq
import sys
from operator import itemgetter

sys.setrecursionlimit(1500)


class TrieNode:
	def __init__(self):
		self.v = ''
		self.next = defaultdict(TrieNode)
		self.count = 0


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		tok = ''
		for ch in word:
			tok += ch
			node = node.next[ch]
			node.v = tok

		node.count += 1

	def find_top_k(self, k, node):
		candidates = []

		if node.count > 0:
			candidates.append((-node.count, node.v))

		for key, child in node.next.items():
			candidates = list(heapq.merge(candidates, self.find_top_k(k, child), key=itemgetter(0, 1)))
		return candidates[:k]


class Solution(object):
	def topKFrequent(self, words, k):
		trie = Trie()
		for w in words:
			trie.insert(w)
		top_ks = trie.find_top_k(k, trie.root)
		return list(map(lambda x: x[1], top_ks))
