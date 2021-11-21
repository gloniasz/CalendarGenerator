from typing import Dict
import constants
import urllib.request, json

# using API provided by: https://date.nager.at/swagger/index.html

class holidayDonwloader:
    address : str = ""
    countries_endpoint : str = ""
    holidays_endpoint : str = "" 
    def __init__(self, address : str = constants.HOLIDAY_API_ADDRESS, countries : str = constants.COUNTRIES_LIST_ENDPOINT, holidays : str = constants.PUBLIC_HOLIDAYS_ENDPOINT) -> None:
        self.setApiAddress(address)
        self.setCountriesListEndpoint(countries)
        self.setHolidaysListEndpoint(holidays)
    
    def setApiAddress(self, address : str):
        self.address = address
    
    def setCountriesListEndpoint(self, countries : str):
        self.countries_endpoint = countries
    
    def setHolidaysListEndpoint(self, holidays : str):
        self.holidays_endpoint = holidays

    def getCountriesDict(self) -> Dict[str, str]:
        countries = {}
        with urllib.request.urlopen(self.address+self.countries_endpoint) as url:
            jsonData = json.loads(url.read().decode())
            for record in jsonData:
                countries[record['name']] = record['countryCode']
        return countries

    def getPublicHolidaysDatesList(self, year, country : str, county : str = ""):
        dates = []
        with urllib.request.urlopen(self.address+self.createHolidayEndpoint(year, country)) as url:
            jsonData = json.loads(url.read().decode())
            for record in jsonData:
                if county == "":
                    dates.append(record['date'])
                elif record['counties'] == None or county in record['counties']:
                    dates.append(record['date'])
        return dates
    
    def createHolidayEndpoint(self, year, country : str):
        return self.holidays_endpoint.replace("_",  str(year), 1).replace("_", country, 1)

hd = holidayDonwloader()
# print(hd.getCountriesDict())
print(hd.getPublicHolidaysDatesList("2021", "DE", "DE-SN"))
