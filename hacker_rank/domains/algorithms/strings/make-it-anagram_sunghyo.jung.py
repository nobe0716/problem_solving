__author__ = 'sunghyo.jung'
import string
d = map(lambda x:{k: x.count(k) for k in string.ascii_lowercase}, [raw_input(), raw_input()])
e = {k: min([d[0][k], d[1][k]]) for k in string.ascii_lowercase}
print sum({k : d[0][k] - e[k] + d[1][k] - e[k] for k in string.ascii_lowercase}.values())