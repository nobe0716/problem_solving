def is_black(x, y):
    return (x + y) % 2 == 1


def is_white(x, y):
    return (x + y) % 2 == 0


def inspect(x1, y1, x2, y2):
    row_size = (x2 - x1 + 1)
    col_size = (y2 - y1 + 1)
    temporal_product = row_size * col_size // 2
    if row_size % 2 == 0 or col_size % 2 == 0:
        return (temporal_product, temporal_product)
    elif is_black(x1, y1):
        return (temporal_product + 1, temporal_product)
    return (temporal_product, temporal_product + 1)


def belong(x1, y1, x2, y2, x3, y3, x4, y4):
    return x3 <= x1 and x2 <= x4 and y3 <= y1 and y2 <= y4


def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    square = max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4)
    if square[0] > square[2] or square[1] > square[3]:
        return None
    if belong(*square, x1, y1, x2, y2) or belong(*square, x3, y3, x4, y4):
        return square
    return None


# Black -> White -> Black
for _ in range(int(input())):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    black, white = inspect(1, 1, n, m)

    t1_black, t1_white = inspect(x1, y1, x2, y2)

    black -= t1_black
    white += t1_black

    t2_black, t2_white = inspect(x3, y3, x4, y4)

    black += t2_white
    white -= t2_white

    intersection_info = intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    if intersection_info:
        b, w = inspect(*intersection_info)
        black += b
        white -= b

    print(white, black)
