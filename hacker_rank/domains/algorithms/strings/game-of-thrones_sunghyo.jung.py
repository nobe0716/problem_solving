__author__ = 'sunghyo.jung'
d = {chr(k): 0 for k in range(65, 91)}
for ch in raw_input().upper():
    d[ch] = d[ch] + 1
c = len(filter(lambda x: x % 2 == 1, d.values()))
print "YES" if c < 2 else "NO"
