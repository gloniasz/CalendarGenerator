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

class header_generator:
    headers : int = []
    def __init__(self, month_data: month_basics) -> None:
        for day in range(0, month_data.days_amount):
            self.headers.append(day % 7 + month_data.day_first)
        pass

mb = month_basics(11, 2021)
headers = header_generator(mb)

print(headers.headers)