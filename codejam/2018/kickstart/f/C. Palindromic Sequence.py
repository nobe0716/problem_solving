"""
wip

## Name of Prob
Palindromic Sequence

## Link
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e07/0000000000051186

## Note
lexicographically k-th smallest; 사전순으로 정렬했을 때 k 번재

## Input
l, n, k
l; (1 <= 26) 사용할 알파벳의 수
n; 글자 길이 제한
k; lexicographically  k-th smallest

## Output
k 번째로 작은(lexicographically smallest) palindromic 문자열의 길이를 구하면 된다.

## Strategy
길이가 N 일 때 만들 수 있는 palindromic 의 수를 계산하면 될 듯 싶음
palindromic 이기 대문에 문자열의 뒤쪽 절반은 앞쪽 절반의 복사
유효한 길이는 (N + 1) // 2 에 해당

palindromic 함을 무시했을 땐
길이 N -> l ^ N 의 가짓수에 해당하는 문자열이 존재

N 이 홀수: l ^ (N // 2) * l 개 표현 가능
N 이 짝수: l ^ (N // 2) 개 표현 가능

홀짝 한 세트가 (l + 1) * l ^ (N // 2)
"""

_DEBUG = True
num_of_test = int(input())


def solve(l, n, k):
    if k <= l:
        return 1
    k -= l
    for i in range(2, n):
        half = i // 2
        if i % 2 == 1:
            k -= (l ** half * l)
        else:
            k -= l ** half

        if k < 0:
            return i
    return 0


for test_num in range(1, num_of_test + 1):
    l, n, k = map(int, input().split())

    solution = solve(l, n, k)
    print("Case #{}: {}".format(test_num, solution))
