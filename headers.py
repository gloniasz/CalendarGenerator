import constants
from month_data import month_basics

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
