#!/usr/bin/py
# Head ends here

# submited

def pairs(a,k):
    s = set(a)
    return sum([i + k in s for i in s])
# submited

# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
