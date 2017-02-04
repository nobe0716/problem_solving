from collections import Counter

def solve(s):
    c = Counter(s)
    #print c.values()
    c = Counter(c.values())
    #print c
    return 'YES' if len(c.values()) <= 2 and len(filter(lambda x: x > 1, c.values())) <= 1 else 'NO'

def submit():
    print solve(raw_input())
def test():
    assert solve('abcdefghijklmnopqrstuvwxyz') == 'YES'
    assert solve('abcdefghijklmnopqrstuvwxyzz') == 'YES'
    assert solve('aabcdefghijklmnopqrstuvwxyzz') == 'NO'
    assert solve('aabcdefghijklmnopqrstuvwxyzzz') == 'NO'
submit()
#test()