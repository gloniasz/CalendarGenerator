import calendar
import constants

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
        for day_nr in range(month_data.days_amount):
            self.headers.append(day_nr % 7 + month_data.day_first)
        pass

    def daysNamesHeader(self, abbr : bool =  False):
        if abbr:
            day_names = constants.DAYS_ABBR
        else:
            day_names = constants.DAYS
        headers_days = []
        for day_nr in range(len(self.headers)):
            headers_days.append(day_names[self.headers[day_nr]])
        return headers_days

    def daysNumbersHeader(self):
        return list(range(1, len(self.headers)+1))

mb = month_basics(11, 2021)
headers = header_generator(mb)

print(headers.daysNamesHeader(True))
print(headers.daysNumbersHeader())
