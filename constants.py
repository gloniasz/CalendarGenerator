HEADING_SEPARATOR = "||"
COLUMN_SEPARATOR = "|"
ROW_ENDING = "\n"

BOLD_STYLE = "*"
ITALIC_STYLE = "_"
UNDERLINE_STYLE = "+"

COLOR_TEXT_BEGIN = "{color:_}"
COLOR_TEXT_END = "{color}"
COLOR_BKG = ""

COLORS = {
    "black" : "#172B4D",
    "dark grey" : "#505F79",
    "light grey" : "#C1C7D0",
    "blue" : "#0747A6",
    "light blue" : "#4C9AFF",
    "green" : "#00875A",
    "pale green" : "57D9A3",
    "red" : "#DE350B",
    "dark orange" : "#FF8B00",
    "light orange" : "#FFAB00",
    "purple" : "#403294",
    "peach" : "#FFBDAD"
}

DAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
DAYS_ABBR = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUN", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
MONTHS_ABBR = ["JAN", "FEB", "MAR", "JUNE", "JULY", "AUG", "SEPT", "OCT", "NOV", "DEC"]
PUBLIC_HOLIDAY_CHECK = "x"

HOLIDAY_API_ADDRESS = "https://date.nager.at/"
COUNTRIES_LIST_ENDPOINT = "api/v3/AvailableCountries"
PUBLIC_HOLIDAYS_ENDPOINT = "api/v3/PublicHolidays/_/_" # /YEAR/COUNTRY_CODE
