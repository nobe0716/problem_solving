"""
wip

## Name of Prob
Specializing Villages

## Link
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e07/0000000000051134

## Note
bidirectional graph
모든 edge 는 다른 length 를 가짐
모든 edge 는 unique 한 vertex pair 로 연결 됨

optimal 한 vertex color tuple이 있을 때,
각 color (fruit | vegetable) 을 반전 시켜도 된다.
=> {vertex A가 fruite 일 경우 찾은 optimal 한 case의 수} x 2
  같은 느낌으로 해결 가능


## Input
v, e: vertex, edge 수
a_i, b_i, l_i: a=>b, b=>a weight가 l

## Output

## Strategy
"""
from collections import defaultdict

_DEBUG = False
num_of_test = int(input())

for test_num in range(1, num_of_test + 1):
    v, e = map(int, input().split())
    g = defaultdict(dict())
    for _ in range(e):
        a, b, l = map(int, input().split())
        g[b][a] = g[a][b] = l

    solution = None
    print("Case #{}: {}".format(test_num, solution))
