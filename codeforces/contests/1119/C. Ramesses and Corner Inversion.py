"""
## Name of Prob
C. Ramesses and Corner Inversion

## Link
https://codeforces.com/contest/1119/problem/C

## Note
NxM matrix, binary value(0 or 1)

operation:
    select submatrix (bigger than 2x2) of A
    invert corner's value

find possibility A can be transformed to B

## Input
n, m
matrix A
matrix B

## Output
Yes|No

## Strategy

count total diff
if total_diff % 4 != 0 print 'No' immediately.

Execute below operations (total_diff // 4) counts
1. Find (i, j, k, l), which a[x][y] != b[x][y] in ([i, j], [k, j], [i, l], [k, l])
    To make it easy, store diff count of rows and cols
    Explorer k, l for i, j if a[i][j] != b[i][j] and row_diff[i] >= 2 and col_diff[j] >= 2
2. assign a[x][y] to b[x][y] and row_diff[x]--, col_diff[y]--

return 'No' if there can be no additional operation and there is remain numbers

---
## revised Strategy

check column, row parity

"""


def solve(n, m, a, b):
    row_count_a, col_count_a = [0] * n, [0] * m
    row_count_b, col_count_b = [0] * n, [0] * m
    for i in range(n):
        for j in range(m):
            if a[i][j] == '1':
                row_count_a[i] += 1
                col_count_a[j] += 1
            if b[i][j] == '1':
                row_count_b[i] += 1
                col_count_b[j] += 1

    return 'Yes' if all(abs(row_count_a[i] - row_count_b[i]) % 2 == 0 for i in range(n)) and all(
        abs(col_count_a[i] - col_count_b[i]) % 2 == 0 for i in range(m)) else 'No'
    # return 'Yes'


n, m = map(int, input().split())
a = [input().split() for _ in range(n)]
b = [input().split() for _ in range(n)]
print(solve(n, m, a, b))
