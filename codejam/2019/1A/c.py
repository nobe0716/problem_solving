"""
## Name of Prob
Alien Rhyme

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05

## Note
같은 postfix로 끝나면 rhymes

## Input
N
S_i (0 <= i)

2 <= N <= 6 for small

## Output
가능한 부분셋의 전체 수

## Strategy
뭔가 단어로 Trie를 만들면 끝날 것 같은 느낌이 듬

trie를 만들면서 해당 단어 까지 쪼개지는 단어가 몇개인지 세다가
두개 | 세개가 나오면 exit. 해당 술르 세면 될 듯?
"""
from collections import defaultdict


class Trie():
	def __init__(self):
		self.next = defaultdict(Trie)
		self.cnt = 0
		self.cur = None


_DEBUG = True
num_of_test = int(input())


def add_word(node, word):
	str = ''
	for ch in word[::-1]:
		str += ch
		node = node.next[ch]
		node.cnt += 1
		node.cur = str


def find_count(node):
	if node.cnt < 2:
		return 0
	subset_count = 0
	for k, v in node.next.items():
		subset_count += find_count(v)
	rest = node.cnt - subset_count
	subset_count += min(rest // 2 * 2, 2)
	return subset_count


for test_num in range(1, num_of_test + 1):
	n = int(input())
	words = [input() for _ in range(n)]

	head = Trie()
	for word in words:
		add_word(head, word)

	solution = 0
	for k, v in head.next.items():
		solution += find_count(v)
	print("Case #{}: {}".format(test_num, solution))
