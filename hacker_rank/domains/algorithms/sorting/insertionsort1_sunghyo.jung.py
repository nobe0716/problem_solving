__author__ = 'sunghyo.jung'


def printAr(ar):
    print str(ar).replace('[', '').replace(']', '').replace(',','')

def insertionSort(ar):
    n = len(ar)

    for i in xrange(n - 1, 0, -1):
        v = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > v:
            ar[j + 1] = ar[j]
            printAr(ar)
            j = j - 1

        if ar[j + 1] == v:
            continue

        ar[j + 1] = v
        printAr(ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)








