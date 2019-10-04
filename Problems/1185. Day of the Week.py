from typing import *

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0

        if year % 4 == 0:
            months = leap_months
        
        for y in range(1971, year):
            if y % 4 == 0:
                days += 366
            else:
                days += 365
        
        for i in range(1, month):
            days += months[i]
        
        days += day + 4 # 1 Jan 1971 is Friday

        return week_days[days % 7]

s = Solution()

assert s.dayOfTheWeek(31, 8, 2019) == "Saturday"
assert s.dayOfTheWeek(18, 7, 1999) == "Sunday"
assert s.dayOfTheWeek(15, 8, 1993) == "Sunday"