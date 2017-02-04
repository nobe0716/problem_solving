__author__ = 'sunghyo.jung'

if __name__ == '__main__':
    v = int(raw_input())
    n = int(raw_input())
    arr = map(int,raw_input().strip().split(' '))

    for i in xrange(n):
        if arr[i] == v:
            print(i)
            break



