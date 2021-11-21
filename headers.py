import constants
from month_data import month_basics

class header_generator:
    headers : int = []
    def setHeaders(self, days_amount: int, day_first: int):
        for day_nr in range(days_amount):
            self.headers.append(day_nr % 7 + day_first)

    def __init__(self, month_data: month_basics =  None) -> None:
        if month_basics is None:
            self.setHeaders(month_data.days_amount, month_data.day_first)
    def __init__(self) -> None:
        pass

    def daysNamesHeader(self, abbr : bool =  False):
        day_names : int = []
        headers_days : int = []
        if abbr:
            day_names = constants.DAYS_ABBR
        else:
            day_names = constants.DAYS
        for day_nr in range(len(self.headers)):
            headers_days.append(day_names[self.headers[day_nr]])
        return headers_days

    def daysNumbersHeader(self):
        return list(range(1, len(self.headers)+1))

mb = month_basics(11, 2021)
headers = header_generator()
headers.setHeaders(30,0)

print(headers.daysNamesHeader(True))
print(headers.daysNumbersHeader())
