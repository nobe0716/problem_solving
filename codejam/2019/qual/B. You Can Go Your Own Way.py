"""
## Name of Prob
You Can Go Your Own Way

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

## Note
미로 탈출, 라이벌과 다른 패스


## Input
N; row, col length of NxN maze
P: len(P) == 2N - 2, move sequence of rival, S: To South, E: To East

## Output
S: maze output sez which differs from that of rival

## Strategy
We need reorder 'E' * (n - 1) + 'S' * (n - 1)
Count num of S, E for given seq
Avoid same num using Greedy (choose direction by maximize different count)
"""

_DEBUG = True
num_of_test = int(input())


def solve(l, seq):
    s_of_seq = e_of_seq = 0
    count = []
    for e in seq:
        if e == 'E':
            e_of_seq += 1
        if e == 'S':
            s_of_seq += 1
        count.append((e_of_seq, s_of_seq))

    new = ''
    s_of_new = e_of_new = 0
    for i in range(2 * l - 2):
        s_of_seq, e_of_seq = count[i]
        if s_of_seq - s_of_new > e_of_seq - e_of_new:
            s_of_new += 1
            new += 'S'
        else:
            e_of_new += 1
            new += 'E'
    return new


def verify(seq, solution):
    def trans_dir(dir):
        return [0, 1] if dir == 'E' else [1, 0]

    pos_origin = [0, 0]
    pos_solution = [0, 0]
    for dir_origin, dir_solution in zip(seq, solution):
        # if pos_origin == [0, 0] and pos_solution == [0, 0]:
        #     continue
        if pos_origin != [0, 0] and pos_origin == pos_solution and dir_origin == dir_solution:
            print(pos_origin, dir_origin)
            return False
        pos_origin = [pos_origin[0] + trans_dir(dir_origin)[0], pos_origin[1] + trans_dir(dir_origin)[1]]
        pos_solution = [pos_solution[0] + trans_dir(dir_solution)[0], pos_solution[1] + trans_dir(dir_solution)[1]]

    return True


for test_num in range(1, num_of_test + 1):
    len_of_seq = int(input())
    seq = input()

    solution = solve(len_of_seq, seq)

    if not verify(seq, solution):
        print('WRONG ANS!')
    print("Case #{}: {}".format(test_num, solution))
