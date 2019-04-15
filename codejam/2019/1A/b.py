"""
## Name of Prob
Golf Gophers

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a

## Note

## Input

## Output

## Strategy
gopher의 수를 M이라고 하자

그리고 each blade가 돌아갔다고 가정을 해

각 gopher가 각 blade를 돌린 수를 18*k_i + C(0<=18) 으로 표현할 수 있다.
각 blade의 delta를 다 더한다. blade간의 delta 합이 M 이랑 같으면 됨!


blade가 변화가 없다 -> 18k
blade 숫자가 d만큼 커졌다. d + 18k
blad 숫자가 d 만큼 작아졌다. (18 - d) + 18k 보장

blade 의 변화를 통해 18k를 제외한 수식을 다 더하자. (<- binary search에서 좌변에 해당)
blade 의 변화 sum을 S + 18k 로 표현 했을 때

S + 18k < M 인 k를 먼저 찾는다.


"""
import random
_DEBUG = True
num_of_test, n, m = map(int, input().split())

for test_num in range(1, num_of_test + 1):
    candidates = []
    for _ in range(n):
        blades = []
        for _ in range(18):
            blades.append(2)
        # [2] * 18
        print(' '.join(map(str, blades)))

        new_blades = map(int, input().split())

        s = 0
        for old_blade, new_blade in zip(blades, new_blades):
            d = new_blade - old_blade
            if d < 0:
                s += (18 + d)
            else:
                s += d
        if s <= m:
            candidates.append(s)
        if s == m:
            break
    # s + 18k
    solution = max(candidates)
    print(solution)
    is_correct = input()
    if is_correct == '-1':
        break

    # print("Case #{}: {}".format(test_num, solution))
