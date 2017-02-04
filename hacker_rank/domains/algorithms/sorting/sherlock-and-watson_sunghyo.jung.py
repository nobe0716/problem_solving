n, k, q = map(int, raw_input().split())
k = k % n
ar = map(int, raw_input().split())
ar = ar[n - k:] + ar[:n - k]
for i in range(q):
    query = int(input()) % n
    print(ar[query])