import re

text = 'Ala ma 3 koty i 2 lwy.'

#nie używać
print(re.match('\d', text))

reg = re.compile('\d')

#tak jak match wszedzie indziej
#jedno pierwsze trafienie
print(re.search(reg, text))

#lista znalezionych wartosci
print(re.findall('\d', text))
#Zbiór obiektów Match
print(re.finditer('\d', text))


print(re.search('Koty', text, re.IGNORECASE))

#zastapienie liczb z w stringu
print(re.sub('\d', '#', text))
print(re.subn('\d', '#', text))

#rozdzielenie stringu
print(re.split('\W', text))

#zawsze kiedy wartość wyrazenia pochodzi ze zmiennej należy skleic warosc escape do wyrazenia
pattern = '/^' + re.escape('Wartość z zewnątrz')
print(pattern)

result = re.search('\d', text)
if result:
    print(result.start())
    print(result.end())
    print(result.span())
    print(result.group())

