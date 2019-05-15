"""
## Name of Prob
Falling Balls

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f2

## Note
match balls to column
ball will consumed from left to right

> it is not necessary to use a minimal number of ramps, or for every ramp to affect the balls

## Input

t
n; num_of_balls
c_i; c[i]: desired number of balls for i-th column

## Output
IMPOSSIBLE or

row_count
grid

## Strategy

For every ball, find slot idx

ball_to_col[i]: idx of column where i-th ball should fall.

h, height of grid is determined by max(abs(ball_to_col[i] - col[i])) cus it stands for the number of lamps to shift

For every ball, make a path from top to bottom
"""
import random


def solve(l, cols):
    if cols[0] == 0 or cols[-1] == 0:
        return None
    ball_idx = 0
    ball_to_col = [0] * l  # ball_to_column[i]; i-th ball should fall to ball_to_col[i]-th column
    for i in range(l):
        # current_stock += 1
        if ball_idx + cols[i] > l:
            return None
        for j in range(ball_idx, ball_idx + cols[i]):
            ball_to_col[j] = i
        ball_idx += cols[i]
    if ball_idx != l:
        return None

    h = max((abs(ball_to_col[i] - i) for i in range(l)))
    grid = [['.'] * l for _ in range(h)]
    for i in range(l):
        current_pos = i
        goal_x = ball_to_col[i]
        for j in range(0, h):
            if goal_x < current_pos:
                grid[j][current_pos] = '/'
                current_pos -= 1
            elif goal_x > current_pos:
                grid[j][current_pos] = '\\'
                current_pos += 1
            else:
                grid[j][current_pos] = '.'
    grid.append(['.'] * l)
    return h + 1, grid


def generate_random_input(l):
    arr = [1] + [0] * (l - 2) + [1]
    for _ in range(l - 2):
        arr[random.randint(0, l - 1)] += 1
    return arr


def verify(l, cols, h, grid):
    actual = [0] * l
    for i in range(l):
        pos = i
        for j in range(h - 1):
            if grid[j][pos] == '/':
                pos -= 1
            elif grid[j][pos] == "\\":
                pos += 1
        actual[pos] += 1
    return cols == actual


_DEBUG = False
if _DEBUG:
    num_of_test = 1000
    for test_num in range(1, num_of_test + 1):
        l = random.randint(2, 100)
        columns = generate_random_input(l)
        solution = solve(l, columns)
        num_of_rows, rows = solution

        if not verify(l, columns, num_of_rows, rows):
            print('# found wrong input')
            print(l)
            print(' '.join(map(str, columns)))
            print('# wrong solution')
            print("Case #{}: {}".format(test_num, num_of_rows))
            for row in rows:
                print(''.join(row))

else:
    num_of_test = int(input())
    for test_num in range(1, num_of_test + 1):
        num_of_balls = int(input())
        columns = list(map(int, input().split()))
        solution = solve(num_of_balls, columns)
        if solution is None:
            print("Case #{}: IMPOSSIBLE".format(test_num))
        else:
            num_of_rows, rows = solution
            print("Case #{}: {}".format(test_num, num_of_rows))
            for row in rows:
                print(''.join(row))
