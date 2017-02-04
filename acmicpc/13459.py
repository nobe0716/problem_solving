# 0; 위로, 1: 오른쪽으로, 2: 아래로, 3:왼쪽으로
def lean(map, n, m, d):
    if d == 0:
        for i in range(n - 1):
            for j in range(m):
                if map[i][j] == '.':
                    idx_of_object = None
                    for k in range(i + 1, n):
                        if map[i][j] == '#':
                            break
                        elif map[i][j] == ''

def able(m, n, m):
    q = [(m, 0)]
    while len(q) > 0:
-
    return 0


n, m = map(int, input().split())
map = [input() for _ in range(n)]
print(able(map, n, m))