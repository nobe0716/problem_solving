__author__ = 'sunghyo.jung'


for t in range(int(input().strip())):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    for i in range(n - 2):
        min_value = min(a[i:])
        min_idx = -1
        for j in range(i, n):
            if a[j] == min_value:
                min_idx = j
                break

        # ... min_idx
        while min_idx > i + 2:
            a[min_idx - 2:min_idx + 1] = a[min_idx - 1:min_idx + 1] + a[min_idx - 2:min_idx - 1]
            min_idx -= 1
        while min_idx != i:
            a[i:i + 3] = a[i + 1:i + 3] + a[i:i + 1]
            min_idx -= 1
    print("YES" if a[n - 3:n] == sorted(a[n - 3:n]) else "NO")