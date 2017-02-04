
def print_v(v):
    print v[:3] + '\n ' + v[3:4] + '\n' + v[4:] + '\n'

def extract_pattern(m, i, j):
    v = m[i][j] + m[i][j + 1] + m[i][j + 2] + m[i + 1][j + 1] + m[i + 2][j] + m[i + 2][j + 1] + m[i + 2][j + 2]
    return sum(map(int, [m[i][j], m[i][j + 1], m[i][j + 2], m[i + 1][j + 1], m[i + 2][j], m[i + 2][j + 1], m[i + 2][j + 2]]))
#    print v
#    print_v(v)
#    return v

s = set()
m = []
v = -100000000000000
for i in xrange(6):
    m.append(raw_input().split())

for i in xrange(4):
    for j in xrange(4):
        #s.add(extract_pattern(m, i, j))
        v = max([v, extract_pattern(m, i, j)])


print v
