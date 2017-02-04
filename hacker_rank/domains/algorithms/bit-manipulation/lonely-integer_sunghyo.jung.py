#!/usr/bin/py
def lonelyinteger(a):
    answer = 0
    a.sort()
    #print "len is " + str(len(a))
    for i in range(0, len(a)):
        #print "i is " + str(i)
        if i == 0:
            if len(a) == 1 or a[i] != a[i+1]:
                answer = a[i]
                break
        elif i == len(a) - 1:
            if a[i] != a[i-1]:
                answer = a[i]
                break
        elif a[i-1] != a[i] and a[i] != a[i+1]:
            answer = a[i];
            break
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
