
from requests import get
from re import search

response = get('http://www.nbp.pl/')

data = search(r'<div>Tabela z dnia (.*)</div>', response.text).group(1)
print(data)






