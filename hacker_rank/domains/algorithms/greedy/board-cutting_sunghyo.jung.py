__author__ = 'sunghyo.jung'
for t in range(int(input())):
    m, n = [int(x) for x in raw_input().split()]
    cy = sorted([int(x) for x in raw_input().split()], reverse=True)
    cx = sorted([int(x) for x in raw_input().split()], reverse=True)

    cost = 0
    y = x = 1

    while len(cy) > 0 and len(cx) > 0:
        if (cy[0] >= cx[0]):
            cost += cy[0] * x
            y += 1
            cy.pop(0)
        else:
            cost += cx[0] * y
            x += 1
            cx.pop(0)

    for c in cy:
        cost += (c * x)
    for c in cx:
        cost += (c * y)
    print(cost % 1000000007)