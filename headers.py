import constants
from month_data import monthBasics

class headerGenerator:
    headers : int = [] # stores week day numbers
    def setHeaders(self, days_amount: int, day_first: int):
        for day_nr in range(days_amount):
            self.headers.append((day_nr + day_first) % 7)

    def __init__(self, month_data: monthBasics =  None) -> None:
        self.headers = []
        if month_data is not None:
            self.setHeaders(month_data.days_amount, month_data.day_first)

    def getDaysNamesHeader(self, abbr : bool =  False):
        day_names : int = []
        headers_days : int = []
        if abbr:
            day_names = constants.DAYS_ABBR
        else:
            day_names = constants.DAYS
        for day_nr in range(len(self.headers)):
            headers_days.append(day_names[self.headers[day_nr]])
        return headers_days

    def getDaysNumbersHeader(self):
        return list(range(1, len(self.headers)+1))

mb = monthBasics(11, 2021)
# headers = headerGenerator()
# headers.setHeaders(30,0)
headers = headerGenerator(mb)

print(headers.getDaysNamesHeader(True))
print(headers.getDaysNumbersHeader())
