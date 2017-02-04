# If there are no elements to the left/right, then the sum is considered to be zero. <- Edge case
def is_positive(a):
    sum_from_home = 0
    sum_from_end = sum(a[1:])
    if sum_from_home == sum_from_end:
        return True
    for i in range(1, len(a)):
        sum_from_home += a[i - 1]
        sum_from_end -= a[i]
        if sum_from_home == sum_from_end:
            return True
    return False

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print ('YES' if is_positive(a) else 'NO')
