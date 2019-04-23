"""
wip

## Name of Prob
D. Beautiful Array

## Link
https://codeforces.com/contest/1155/problem/D

## Note
Beauty of array is the maximum sum of some consecutive subarray of this array (this subarray may be empty).
For example, the beauty of the array [10, -5, 10, -4, 1] is 15, and the beauty of the array [-3, -5, -1] is 0.

You may choose at most one consecutive subarray of a and multiply all values contained in this subarray by x.
You want to maximize the beauty of array after applying at most one such operation.

## Input
n and x (1≤n≤300000,−100≤x≤100)

## Output
the maximum possible beauty of array a after multiplying all values belonging to some consecutive subarray x.

## Strategy
If x > 0, multiply x to all and get beauty of array
If x < 0, multiply x to original minimized interval?

Since I use python so that multiply x to every elements of a
and get maximum consecutive sum
"""


def solve(n, x, a):
    if x > 0:
        for i in range(n):
            a[i] *= x
        current_sum = a[0]
        beauty = 0
        for i in range(1, n):
            current_sum = max(a[i], current_sum + a[i])
            beauty = max(beauty, current_sum)
        return beauty
    else:
        start = end = 0
        minimum_sum = a[start]
        for i in range(1, n):
            if a[i] < minimum_sum + a[i]:
                start = end = i

                minimum_sum = a[start]
            else:
                minimum_sum += a[i]
                end = i
        if minimum_sum < 0:
            for i in range(start, end + 1):
                a[i] *= x

        current_sum = a[0]
        beauty = 0
        for i in range(1, n):
            current_sum = max(a[i], current_sum + a[i])
            beauty = max(beauty, current_sum)
        return beauty


assert solve(5, -2, list(map(int, '-3 8 -2 1 -6'.split()))) == 22
assert solve(12, -3, list(map(int, '1 3 3 7 1 3 3 7 1 3 3 7'.split()))) == 42
assert solve(5, 10, list(map(int, '-1 -2 -3 -4 -5'.split()))) == 0
assert solve(10, 100, list(map(int,
                               '1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000'.split()))) == 1000000000000

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, x, a))
