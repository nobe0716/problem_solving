__author__ = 'sunghyo.jung'
import datetime

d1,m1,y1 = map(int, raw_input().strip().split())
d2,m2,y2 = map(int, raw_input().strip().split())
returned_date = datetime.date(y1, m1, d1)
expected_date = datetime.date(y2, m2, d2)

fine = 0
if expected_date < returned_date:
    if y1 == y2 and m1 == m2:
        fine = (d1 - d2) * 15
    elif y1 == y2:
        fine = (m1 - m2) * 500
    else:
        fine = 10000
print fine

