# 2022-03-27 20:48:41.001509
# https://codeforces.com/problemset/problem/1539/D
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, prices):
    prices = sorted(prices, key=lambda x: x[1])
    cur_buy = 0

    money = 0
    back_pointer = n - 1

    for i in range(n):
        if prices[i][0] == 0:
            continue
        while cur_buy < prices[i][1] and back_pointer >= i:
            if cur_buy + prices[back_pointer][0] <= prices[i][1]:
                cur_buy += prices[back_pointer][0]
                money += 2 * prices[back_pointer][0]
                prices[back_pointer][0] = 0
                back_pointer -= 1
            else:
                num_to_buy = prices[i][1] - cur_buy

                cur_buy += num_to_buy
                money += 2 * num_to_buy
                prices[back_pointer][0] -= num_to_buy

        money += prices[i][0]
        cur_buy += prices[i][0]
        prices[i][0] = 0
    return money


n = int(input().strip())
prices = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    prices.append([a, b])

print(proc(n, prices))
