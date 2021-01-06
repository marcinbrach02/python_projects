import re

text = 'Od 2012-03-23 do 2015-04-24'

reg = '(?P<rok>\d{4})-(?P<miesiąc>\d{2})-(?P<dzień>\d{2})' #?P<> - dodanie nazwy grupy

match = re.search(reg, text)

print(match.group(0))
print(match.group(1)) #pierwsza grupa

#subgrup
print(match.groups()) #w perwszym matchu 1 grupa

print(re.findall(reg, text))

#finditer == searchall
for match in re.finditer(reg, text):
    print(match.group(2))
    print(match.group('dzień'))
    print(match.groupdict())

html = """
<address>
    <country>Polska</country>
    <city>Warszawa</city>
</address>
"""

match = re.search('<city>(.*)</city>', html)  #dowolny znak 0 lub wiecj razy

print(match.group(1))

match = re.search(r'<(city)>(?P<miasto>.*)</\1>', html)

print(match.group('miasto'))



