n = input()
a = list(map(int, input().split()))
limit = float('inf')
current = 0
for e in a[::-1]:
    stock_to_buy = max(min(e, limit - 1), 0)
    limit = stock_to_buy
    current += stock_to_buy
print(current)
