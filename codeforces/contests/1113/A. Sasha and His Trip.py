n, v = map(int, input().split())

t = [0] + [float('inf')] * n
current_fuel = 0
for i in range(1, n + 1):
    required_gas = (n - i)
    fuel_to_buy = min(required_gas, v) - current_fuel
    current_fuel += fuel_to_buy - 1
    t[i] = t[i - 1] + fuel_to_buy * i
    # print(i, required_gas, fuel_to_buy, t)
# print(t)
print(t[n])
