# Returns days of the week

import calendar

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dayNumber = calendar.weekday(year, month, day)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
        return (days[dayNumber])

print(Solution().dayOfTheWeek(3, 2, 2009))