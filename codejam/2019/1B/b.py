"""
wip

## Name of Prob
Draupnir

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122837

## Note
There is 6 types of ring (1-day ... 6-day)
i-day Ring doubles after i days, (0 <= r_i <= 100)

## Interactive

<< D (1 <= D <= 500)
>> C (total_num_ring % 2 ** 63)

pass D for w (w = 6 for simple, w = 2 for large)

<< r_1 r_2 r_3 r_4 r_5 r_6 (r_i ; initial num of ring)
>> result (result 1 if correct -1 else)


## Output
figure out initial num of rings for each type

## Strategy

### Small

send D from 1 to 6
for each D, we can figure out initial R_i

d[2] = r[1]4 + r[2]2 + r[3] + r[4] + r[5] + r[6]
d[3] = r[1]8 + r[2]2 + r[3]2 + r[4] + r[5] + r[6]
d[4] = r[1]16 + r[2]4 + r[3]2 + r[4]2 + r[5] + r[6]
d[5] = r[1]32 + r[2]4 + r[3]2 + r[4]2 + r[5]2 + r[6]
d[6] = r[1]64 + r[2]8 + r[3]4 + r[4]2 + r[5]2 + r[6]2
d[7] = r[1]128 + r[2]8 + r[3]4 + r[4]2 + r[5]2 + r[6]2

# d[7] - d[6] = r[1] * 64
r[1] = (d[7]-d[6]) // 64 # get r[1]
# d[3] - d[2] = r[1] * 4 + r[3]
r[3] = d[3] - d[2] - r[1] * 4 # get r[3]
# d[6] - d[2] * 2 = r[1]56 + r[2]4 + r[3]2
r[2] = (d[6] - d[2] * 2 - r[1] * 56 - r[3] * 2) // 4 # get r[2]
r[4] = d[4] - d[3] - r[2] * 2 - r[1] * 8 # get r[4]
r[5] = d[5] - d[4] - r[1] * 16 # get r[5]
r[6] = d[6] - d[5] - r[1] * 32 - r[2] * 4 - r[3] * 2 # get 4[6]
"""

_DEBUG = True
num_of_test, w = map(int, input().split())
for test_num in range(1, num_of_test + 1):
    if w == 6:
        d = [None] * 501
        r = [None] * 7
        for i in range(2, 8):
            print(i)
            d[i] = int(input())

        # d[7] - d[6] = r[1] * 64
        r[1] = (d[7] - d[6]) // 64  # get r[1]
        # d[3] - d[2] = r[1] * 4 + r[3]
        r[3] = d[3] - d[2] - r[1] * 4  # get r[3]
        # d[6] - d[2] * 2 = r[1]56 + r[2]4 + r[3]2
        r[2] = (d[6] - d[2] * 2 - r[1] * 56 - r[3] * 2) // 4  # get r[2]
        r[4] = d[4] - d[3] - r[2] * 2 - r[1] * 8  # get r[4]
        r[5] = d[5] - d[4] - r[1] * 16  # get r[5]
        r[6] = d[6] - d[5] - r[1] * 32 - r[2] * 4 - r[3] * 2  # get 4[6]
        print(' '.join(map(str, r[1:])))
        r = input()
    else:
        print('0 0 0 0 0 0')
        r = input()
