# 2022-07-17T14:49:16Z

# up right down left

MV = 10 ** 5


def proc(n, rows):
    def merge(rec1, rec2):
        if rec1[0] > rec2[0]:
            rec1, rec2 = rec1, rec2

        nx1 = max(rec1[0], rec2[0])
        ny1 = max(rec1[1], rec2[1])
        nx2 = min(rec1[2], rec2[2])
        ny2 = min(rec1[3], rec2[3])

        if nx1 > nx2 or ny1 > ny2:
            return None
        return [nx1, ny1, nx2, ny2]

    rec = [- MV, - MV, MV, MV]  # x1, y1, x2, y2
    for x, y, f1, f2, f3, f4 in rows:
        # f1 - up(x-1) / f2 - right(y+1) / f3 - down(x+1) / f4 = left(y-1)
        cur_rec = [x, y, x, y]
        if f1 == 1:
            cur_rec[0] = - MV
        if f2 == 1:
            cur_rec[3] = MV
        if f3 == 1:
            cur_rec[2] = MV
        if f4 == 1:
            cur_rec[1] = -MV

        # merge rec and cur_rec
        rec = merge(rec, cur_rec)
        if not rec:
            return None

    return rec[0], rec[1]


for _ in range(int(input())):
    n = int(input())
    rows = []
    for _ in range(n):
        row = map(int, input().split())
        rows.append(row)
    ans = proc(n, rows)

    if not ans:
        print(0)
    else:
        print(1, ' '.join(map(str, ans)))
