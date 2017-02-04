from __future__  import print_function
import random
#map(lambda x: print(x, sep='', end=''), range(1, int(raw_input()) + 1))

print '5'
print '3 3'
print '-1 0 1'
print '4 2'
print '-1 0 1 2'
print '5 3'
print '-4 0 2 4 6'
print '6 4'
print '-6 -3 -1 0 2 4'
print '7 5'
print '-1 0 3 4 5 6 7'

def generate():
    sol = ['YES', 'NO', 'YES', 'NO', 'YES']
    t = 5
    print ('print(\'' + str(t) + '\')')
    for i in xrange(t):
        n = random.randrange(3, 10)
        k = random.randrange(1, n)
        a = []

        print ('print(\'' + str(n) + ' ' + str(k) + '\')')
        print ('print(\'', end='')
        s = sol[i]
        n_positive = 0
        if s == 'YES': # needs non-positive less more than k
            n_positive = random.randrange(0, k)
        else: # needs non-positive value more than k
            n_positive = random.randrange(k, n)

        for j in xrange(n_positive):
            a.append(random.randrange(-20, 1))
        for j in xrange(n - n_positive):
            a.append(random.randrange(1, 20))
        map(lambda x: print (x, end=' '), a)
        print ('\')')
def test():
    t = int(raw_input())
    for i in xrange(t):
        n, k = map(int, raw_input().split())
        a = map(int, raw_input().split())
        print ('NO' if len(filter(lambda x: x <= 0, a)) >= k else 'YES')

'''
generate()
print('5')
print('6 3')
print('0 8 16 10 6 3 ')
print('5 3')
print('-9 -2 -2 -4 15 ')
print('5 3')
print('-17 6 2 9 16 ')
print('6 1')
print('-12 -17 -14 -18 12 5 ')
print('3 2')
print('5 5 12 ')
'''
test()