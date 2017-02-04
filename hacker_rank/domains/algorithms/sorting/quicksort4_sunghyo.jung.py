__author__ = 'sunghyo.jung'
count_qsort = 0

n = int(input())
ar = [int(x) for x in input().split()]
ar1 = ar.copy()
ar2 = ar.copy()

def partition(ar, l, r):
    pivot = ar[r]
    pi = l
    cnt = 0
    for i in range(l, r):
        if ar[i] < pivot:
            #print('swap(%d <-> %d)' % (ar[i], ar[pi]))
            ar[i], ar[pi] = ar[pi], ar[i]
            cnt += 1
            pi += 1
    #print('swap(%d <-> %d)' % (ar[n - 1], ar[pi]))
    ar[r], ar[pi] = ar[pi], ar[r]
    cnt += 1
    return cnt, ar, pi

def qsort(n, ar):
    l = 0
    r = n - 1
    q = list()
    q.append([l, r])
    swaps = 0
    while len(q) > 0:
        l, r = q.pop(0)
        cnt, ar, pi = partition(ar, l, r)
        swaps += cnt
        if pi - l >= 2:
            q.append([l, pi - 1])
        if r - pi >= 2:
            q.append([pi + 1, r])
    return swaps, ar

def isort(n, ar):
    swaps = 0
    for i in range(1, n):
        p = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > p:
            ar[j + 1] = ar[j]
            swaps += 1
            j -= 1
        ar[j + 1] = p
    return swaps, ar


q_cnt, q_result = qsort(n, ar1)
i_cnt, i_result = isort(n, ar2)
print(i_cnt - q_cnt)
'''
print(q_result)
print(q_cnt)

print(i_result)
print(i_cnt)
'''