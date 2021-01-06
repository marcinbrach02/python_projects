import re

text = 'Ala ma 3 koty i 2 lwy.'

print(re.search('^A', text)) #daszek oznacza poczatek od litery A
print(re.search('y$', text)) #koniec od y
print(re.search('^[AB]]', text)) #zaczyna sie od A lub B
print(re.search('^[A-Z]]', text)) #zakres od A do Z
print(re.search('[0-9]]', text)) #ciąg cyfr od 0 do 9

text = 'Ala ma 00 675 koty'
text = 'Ala ma 00-675 koty'
text = 'Ala ma 00|675 koty'

print(re.search('[0-9][0-9]-[0-9][0-9][0-9]', text)) #kod pocztowy
print(re.search('\d\d-\d\d\d', text)) #\d jest synonimem cyfry [0-9]
print(re.search('[0-9][0-9][^0-9][0-9][0-9]', text)) #nie cyfra
print(re.search('\d\d\D\d\d\d', text)) #nie cyfra
print(re.search('\d{2}\D\d{3}', text)) #pomnozenie tego co jest przed klamerką(liczba cyfr)

text = 'Rok 1999 był czasami 97 ale tylko 1 raz.'
print(re.findall('\d{2,4}', text)) #liczba wystąpień od 2 do 4 cyfr
print(re.findall('\d{1,}', text)) #1 lub wiecej
print(re.findall('\d+', text)) #1 lub wiecej
print(re.findall('\d{,2}', text)) #do 2

text = '99-12-31, 2017-04-03, 81/02/12'
print(re.findall('\d{2,4}[\-/]\d{2}[\-/]\d{2}]', text)) #daty [\-/]




