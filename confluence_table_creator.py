import constants
from month_data import monthBasics
from headers import headerGenerator
from holidays_downloader import holidayDonwloader

class tableGenerator:
    # pass month in range 1-12
    def createCounfluenceHeaderMonth(year, month : int, month_abbr : bool = False, heading_separator : str = constants.HEADING_SEPARATOR):
        if month < 1 or month > 12:
            raise IndexError
        if month_abbr:
            month_str = constants.MONTHS_ABBR[month-1]
        else:
            month_str = constants.MONTHS[month-1]
        return heading_separator + month_str + " " + str(year) + heading_separator      

    def createConfluenceDayHeaderString(header, header_str : str = " ", heading_separator : str = constants.HEADING_SEPARATOR, column_separator : str = constants.COLUMN_SEPARATOR, boldening : str = constants.BOLD_STYLE):
        formattedHeader = heading_separator + header_str + column_separator
        for column in header:
            formattedHeader = formattedHeader + boldening + str(column) + boldening + column_separator
        return formattedHeader

    def createColouredWeekends(header, color : str = constants.COLORS['red'], color_tag_begin :  str = constants.COLOR_TEXT_BEGIN, color_tag_end : str = constants.COLOR_TEXT_END):
        headersFormatted = []
        color_tag_begin_formatted = color_tag_begin.replace("_", color, 1)
        for day in header:
            if day == constants.DAYS[5] or day == constants.DAYS[6] or day == constants.DAYS_ABBR[5] or day == constants.DAYS_ABBR[6]:
                headersFormatted.append(color_tag_begin_formatted + day + color_tag_end)
            else:
                headersFormatted.append(day)
        return headersFormatted
    
    def createEmployeeRow(name : str, days_amount, holiday_data = [], holiday_check : str = constants.PUBLIC_HOLIDAY_CHECK, heading_separator : str = constants.HEADING_SEPARATOR, column_separator : str = constants.COLUMN_SEPARATOR, boldening : str = constants.BOLD_STYLE):
        employeeRow = heading_separator + name + column_separator
        for day in range(1, days_amount+1):
            if day in holiday_data:
                employeeRow = employeeRow + holiday_check + column_separator
            else:
                employeeRow = employeeRow + " " + column_separator
        return employeeRow

    def createHolidaysForMonthList(year, month, country : str, county : str =""):
        return holidayDonwloader().getPublicHolidaysForMonthList(year, month, country, county)

mb = monthBasics(1, 2022)
headers = headerGenerator(mb)

print(tableGenerator.createCounfluenceHeaderMonth(mb.year, mb.month_number))
print(tableGenerator.createConfluenceDayHeaderString(headers.getDaysNumbersHeader(), "Name"))
print(tableGenerator.createConfluenceDayHeaderString(tableGenerator.createColouredWeekends(headers.getDaysNamesHeader(True))))
print(tableGenerator.createEmployeeRow("Feliks Feliksiński", mb.days_amount, tableGenerator.createHolidaysForMonthList(mb.year, mb.month_number, "PL")))