"""
## Name of Prob
Building Palindromes

## Link
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/0000000000119866

## Note
given string s
receive q queries [start, end] inclusive
return the number of interval which makes palindrome


# 12321
# 21312

## Input
t
n q
original string
l_i, r_i queries

## Output
the total num of palindrome which can be produced by given intervals

## Strategy

### make a table t[i][j]

t[i][j] ; 1 if [i...j] can be palindrome by rearranging else 0

### how to figure out t[i][j]

given seq[i...j] can be palindrome if there is at most one alphabet whose count is odd

TC to figure out T[i][j] will be O( 26(size of key, validate possibility) ) = O(1)
so T can be constructed in O(N^2) times
"""
from collections import Counter

_DEBUG = True
num_of_test = int(input())


def construct_table(n, s):
    # left-padding cus given query will be 1-indexed
    s = ' ' + s
    t = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        c = Counter()
        for j in range(i, n + 1):
            c[s[j]] += 1
            if sum(1 if v % 2 == 1 else 0 for v in c.values()) > 1:
                continue
            l = j - i + 1
            t[i][j] = 1
            # t[i][j] = math.factorial(l // 2)
            # for v in c.values():
            #     t[i][j] //= (math.factorial(v // 2))
    return t


for test_num in range(1, num_of_test + 1):
    n, q = map(int, input().split())
    s = input()
    t = construct_table(n, s)
    solution = sum(t[i][j] for i, j in (map(int, input().split()) for _ in range(q)))
    print("Case #{}: {}".format(test_num, solution))
