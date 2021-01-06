
login = input('Podaj login: ')
email = input('Podaj email: ')

plik = open('rekordy.dat', 'r+', encoding='utf-8')

emaile = []

for linia in plik:
    emaile.append(linia.strip().split(' ')[1])

if email in emaile:
    plik.write(f'{login}{email}\n')
else:
    print('email istnieje')

