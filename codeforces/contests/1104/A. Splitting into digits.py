n = int(input())

for i in range(9, 0, -1):
    if n % i == 0:
        count = (n // i)
        print(count)
        print(' '.join([str(i)] * count))
        exit(0)
