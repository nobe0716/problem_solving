__author__ = 'sunghyo.jung'

# https://www.hackerrank.com/challenges/largest-permutation

if __name__ == '__main__':
    n, k = map(int,raw_input().strip().split(' '))
    arr = map(int,raw_input().strip().split(' '))
    i = 0
    while k > 0 and i < n:
        maxi = max(arr[i:])
        j = arr[i:].index(maxi) + i

        if arr[i] < arr[j]:
            k -= 1
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    print str(arr).replace("[", "").replace(",", "").replace("]", "")
