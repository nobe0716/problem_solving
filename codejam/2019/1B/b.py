"""
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

### large
d[question] = sum( (r[i] * 2 ** (question // 2)) for i in range(1, 7) ) % (2 ** 63)
so if we give large number, some r[i] will not affect response if (question // i) >= 63
and 0 <= r[i] <= 100 <= 2 ** 7. it means that if each ring has distance more than 2 ** 7,
we can know multiple value of r[i]

suppose question == 200

d[200] = r[1] * 2 ** 200 + r[2] * 2 ** 100 + r[3] * 2 ** 66 + r[4] * 2 ** 50 + r[5] * 2 ** 40 + r[6] * 2 ** 33

let d[200] = k, then r[4], r[5] and r[6] will be evaluated by below equations.
r[4] = k // (2 ** 50)
r[5] = (k - r[4] * 2 ** 50) // (2 ** 40)
r[6] = (k - r[4] * 2 ** 50 - r[5] * 2 ** 40) // (2 ** 33)

after then, we should choose relatively small number to find r[1] to r[3] that question // 2 - question // 3 >= 7

suppose question == 50

d[50] = r[1] * 2 ** 50 + r[2] * 2 ** 25 + r[3] * 2 ** 16 + r[4] * 2 ** 12 + r[5] * 2 ** 10 + r[6] * 2 ** 8
let k = d[50] - (r[4] * 2 ** 12 + r[5] * 2 ** 10 + r[6] * 2 ** 8), then r[1], r[2], and r[3] will be...
r[1] = k // (2 ** 50)
r[2] = (k - r[1]) // (2 ** 25)
r[3] = (k - r[1] - r[2]) // (2 ** 16)

and do some performance tuning to fast evaluation

"""
_DEBUG = True
num_of_test, w = map(int, input().split())
r = [None] * 7
for test_num in range(1, num_of_test + 1):
    print(200)
    d_200 = int(input())
    d_200 //= 2 ** 33
    r[6] = d_200 % 2 ** 7
    d_200 //= 2 ** 7
    r[5] = d_200 % 2 ** 7
    d_200 //= 2 ** 10
    r[4] = d_200

    print(50)
    d_50 = int(input()) - (r[4] * 2 ** 12 + r[5] * 2 ** 10 + r[6] * 2 ** 8)
    d_50 //= 2 ** 16
    r[3] = d_50 % 2 ** 7
    d_50 //= 2 ** 9
    r[2] = d_50 % 2 ** 7
    d_50 //= 2 ** 25
    r[1] = d_50

    print(' '.join(map(str, r[1:])))
    response = input()
