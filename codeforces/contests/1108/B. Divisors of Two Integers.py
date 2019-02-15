n = int(input())
s = list(map(int, input().split()))
x = max(s)
divisors = []
for i in range(1, x + 1):
    if x % i == 0:
        s.remove(i)
y = max(s)
print(x, y)
