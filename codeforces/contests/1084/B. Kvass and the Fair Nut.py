n, s = list(map(int, input().split()))
v = list(map(int, input().split()))

total_kvass = sum(v)
if total_kvass < s:
    print(-1)
    exit(0)

r = min((total_kvass - s) // n, sorted(v)[0])
print(r)
