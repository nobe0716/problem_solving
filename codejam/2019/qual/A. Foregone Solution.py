"""
## Name of Prob
You Can Go Your Own Way

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

## Note
4를 포함하지 않으면서 합이 N 인걸 찾아야 함

## Input
N jam coins

## Output
two positive integer a, b which meets a + b === n

## Strategy
positive integer 이기만 하면 되니까

10 이나 11 , 1, 0 같은 str 에 대한 특수 처리만 해주면 된다.
n이 11로 시작 할 때는 b에는 leading zero 를 넣지 않는 방식으로 구현

아래 로직에서 i < len(n) - 1 조건을 넣었지만
사실은 i == 0 일 때만 고려해도 답은 나올 듯
"""

_DEBUG = True
num_of_test = int(input())


def solve(n):
    a = []
    b = []
    i = 0
    while i < len(n):
        if i < len(n) - 1 and n[i:i + 2] == '10':
            if i != 0:
                a.append(0)
                b.append(0)
            a.append(5)
            b.append(5)
            i += 2
        elif i < len(n) - 1 and n[i:i + 2] == '11':
            if i != 0:
                b.append(0)
            a.append(1)
            a.append(0)
            b.append(1)
            i += 2
        elif n[i] == '0':
            a.append(0)
            b.append(0)
            i += 1
        elif n[i] == '1':
            a.append(0)
            b.append(1)
            i += 1
        else:
            current_digit = int(n[i])
            for j in range(1, current_digit):
                if current_digit - j != 4:
                    a.append(current_digit - j)
                    b.append(j)
                    break
            i += 1
    return ''.join(map(str, a)), ''.join(map(str, b))


for test_num in range(1, num_of_test + 1):
    num = input()
    solution = solve(num)
    print("Case #{}: {} {}".format(test_num, solution[0], solution[1]))
