from datetime import date
from datetime import timedelta

d, m, y = map(int, raw_input().split())
actual_date = date(y, m, d)
d, m, y = map(int, raw_input().split())
expected_date = date(y, m, d)

delta = actual_date - expected_date
if actual_date <= expected_date:
    print 0
elif expected_date.year == actual_date.year and expected_date.month == actual_date.month:
    print delta.days * 15
elif expected_date.year == actual_date.year:
    print (actual_date.month - expected_date.month) * 500
else:
    print 10000
