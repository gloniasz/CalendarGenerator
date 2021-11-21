import constants
from month_data import monthBasics
from headers import headerGenerator
from holidays_downloader import holidayDonwloader

class tableGenerator:
    def createConfluenceHeaderString(header, name : bool = False, heading_separator : str = constants.HEADING_SEPARATOR):
        if name:
            formattedHeader = heading_separator + "Name" + heading_separator
        else:        
            formattedHeader = heading_separator + " " + heading_separator
        for column in header:
            formattedHeader = formattedHeader + str(column) + heading_separator
        return formattedHeader
    def createConfluenceHeader2ndRowString(header, heading_separator : str = constants.HEADING_SEPARATOR, column_separator : str = constants.COLUMN_SEPARATOR, boldening : str = constants.BOLD_STYLE):
        formattedHeader = heading_separator + " " + column_separator
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
            employeeRow = employeeRow + " " + column_separator
        return employeeRow

mb = monthBasics(11, 2021)
headers = headerGenerator(mb)

print(tableGenerator.createConfluenceHeaderString(headers.getDaysNumbersHeader(), True))
print(tableGenerator.createConfluenceHeader2ndRowString(tableGenerator.createColouredWeekends(headers.getDaysNamesHeader(True))))
print(tableGenerator.createEmployeeRow("Feliks Feliksiński", mb.days_amount))