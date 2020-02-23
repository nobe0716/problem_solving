import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # datetime.datetime.strptime()
        FORMAT = '%Y-%m-%d'
        return abs((datetime.datetime.strptime(date2, FORMAT) - datetime.datetime.strptime(date1, FORMAT)).days)


s = Solution()
assert (s.daysBetweenDates(date1="2019-06-29", date2="2019-06-30") == 1)
assert s.daysBetweenDates(date1="2020-01-15", date2="2019-12-31") == 15
