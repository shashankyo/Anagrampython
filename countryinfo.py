import string
from countryinfo import CountryInfo
from matplotlib.pyplot import text

from countryinfo import CountryInfo
country = CountryInfo("china")
print(country.alt_spellings())
print(country.capital())
print(country.currencies())
print(country.languages())
print(country.borders())