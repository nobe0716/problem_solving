a, b = int(input(), 2), int(input(), 2)
c = 0
MOD = 1000000007
for i in range(314159):
    c += (a ^ (b << i)) % MOD
    if i % 10 == 0:
        c %= MOD

print(c % MOD)
