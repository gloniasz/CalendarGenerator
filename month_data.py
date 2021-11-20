import calendar
class month_basics:
    month_number : int = 0
    year : int = 0
    days_amount : int = 0
    day_first : int = 0
    def __init__(self, month_number, year) -> None:
        self.month_number = month_number
        self.year = year
        self.days_amount = calendar.monthrange(self.year, self.month_number)[1]
        self.day_first = calendar.weekday(self.year, self.month_number,1)
