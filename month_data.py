import calendar
class monthBasics:
    month_number : int = 0
    year : int = 0
    days_amount : int = 0
    day_first : int = 0
    def __init__(self, month_number, year) -> None:
        self.month_number = month_number
        self.year = year
        self.days_amount = calendar.monthrange(self.year, self.month_number)[1]
        self.day_first = calendar.weekday(self.year, self.month_number, 1)
    
    def __str__(self) -> str:
        return "monthBasics: {month_number : " + str(self.month_number) + ", year : " + str(self.year) + ", days_amount: " + str(self.days_amount) + ", day_first: " + str(self.day_first) + "}"

mb = monthBasics(11,2021)
print(mb)