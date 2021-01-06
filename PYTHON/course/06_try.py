
try:
    v = float(input('Podaj liczbę: '))
    print(20 / v)
except ValueError:
    print('Błąd konwersji')
except ZeroDivisionError:
    print('Błąd dzielenia')
except:
    print('Nie znany błąd')
finally:
    print('Koniec!')



