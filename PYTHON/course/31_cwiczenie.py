import requests
import xml.etree.ElementTree as ET


response = requests.get('http://www.nbp.pl/kursy/xml/lasta.xml')
data = ET.fromstring(response.text)

for pozycja in data.iter('pozycja'):
    if pozycja.find('kod_waluty').text == 'USD':
        pass


przeliczniki = [ (pozycja.find('kod_waluty').text, pozycja.find('kurs_sredni').text)
                  for pozycja in data.iter('pozycja') ]

print(przeliczniki)


pln = float(input('Podaj wartosc w PLN: '))
kod = input('Podaj kod waluty: ')

wal = float((data.find(f'.//kurs_sredni/..[kod_waluty="{kod}"]/kurs_sredni').text).replace(',', '.'))

wynik = pln/wal

print(f"{pln} PLN to {kod} = {str(wynik)[:4]}")



