#  D. The Fair Nut and the Best Path

http://codeforces.com/contest/1084/problem/D

## 요약
sub graph에서 얻을 수 있는 gasoline 을 maximize 하는 문제이다.

## Fail #1  
Wrong answer on test 6

input
```
10
67 9 7 2 33 5 1 7 43 55
2 4 38
2 5 77
9 8 91
9 5 8
10 5 4
2 6 49
9 1 5
7 5 100
3 10 13
```
Output
```
105
```
Answer
```
181
```

## Analyze #1
문제를 잘 못 해석했다.
directed graph 가 아닌데, edge 에 방향성이 있다는 것으로 간주
문제에선 `It is guaranteed that graph of road connectivity is a tree.` 라고 하는데,
이는 cyclic 이 없다는 것만을 보증

10->5->9->1 route 를 타게 되면 181이 됨

bfs를 다르게 설계 할 필요가 있음

## Resolve #1 
BFS 에서 state를 가지고 다니기로 함.
(current_gasoline, visited_node) 을 토대로,
현재 state에서 unvisit 인 영역에 대해 추가 탐색

## Fail #2
Wrong answer on test 9

Input
```
10
81 34 31 38 69 62 54 18 72 29
4 8 12
2 9 25
4 5 17
5 7 35
10 1 13
9 3 53
7 6 22
1 6 82
3 10 42
```
Output
```
181
```
Answer
```
187
```

## Analyze #2
node i 에 도달했을 때의 maximum gasoline 을 전역 변수로 두고,
탐색에서 edge를 cut하는 방식을 사용,
케이스에 따라 최적해를 포함하는 루트가 탐색에서 제외되는 경우가 생긴다.

###  Resolve #2
가능한 모든 sub graph route를 다 순회하도록 구현 변경
`gasoline < cost` 라서 edge 를 이용하지 못 하는 경우 빼곤, 다 순회

## Fail #3
Time limit exceeded on test 14

n의 upper bound가 3*10^5 라 당연한 결과

## Resolve #3