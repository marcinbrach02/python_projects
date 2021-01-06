import json
import sys
import re


str = 'Buchanan (01.07.1999): Reims 100,00 zł'

reg = r'(?P<nazwisko>\w+) .(?P<data>\d{2}.\d{2}.\d{4}).. (?P<miasto>\w+) (?P<wartosc>\d{,4}.\d{2})'


#print(re.search(reg, str).groups())

plik = open('dump.dat', encoding='cp1250')
text = plik.read()

match = re.search(reg, text)
print(match.groups())


d = []
for match in re.finditer(reg, text):
    d.append(match.groupdict())


print(json.dump(d, open('dane.json', 'w', encoding='cp1250'), indent=4, ensure_ascii=False))


#reg = r'(?P<nazwisko>\w+) \((?P<data>.*)\): (?P<miasto>\w) (?P<wartość>.*) zł'

# data = [ m.groupdict() for m in re.finditer(reg, open('dump.dat').read()) ]
#
# json.dump()

