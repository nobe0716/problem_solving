__author__ = 'sunghyo.jung'
import math

def is_prime(n):
    if n == 1:
        return False
    for i in xrange(2, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            return False
    return True

for i in xrange(int(raw_input())):
    if not is_prime(int(raw_input())):
        print 'Not prime'
    else:
        print 'Prime'
