
def wstaw(imie, nazwisko = '', email = ''):
    pass

rekord = {'imie': 'tekst', 'email': 'ea@asd.pl'}

wstaw(imie=rekord["imie"], email=rekord['email'])
wstaw(**rekord)


def wstaw(imię, nazwisko, **kwargs): #wymagane bez domyslnej wartosci
    print(kwargs)

wstaw('test', 'test', address='ddd') #do kwargs trafiaja pozostałe argumenty jako słownik

rekord = {
    'imię': 'test',
    'email': 'aa@ww.pl',
    'nazwisko': 'ddd',
    'adres': 'ddd'
}

wstaw(**rekord) # ** - kwargs




