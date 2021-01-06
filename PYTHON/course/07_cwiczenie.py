
try:
    z1 = input('Podaj wartość 1: \n')
    z2 = input('Podaj wartość 2: \n')
    w = float(z1) / float(z2)
    print('Wynikiem dzielenia jest: ' + str(w))
except ValueError:
    print('Błąd konwersji')
except ZeroDivisionError:
    print('Błąd dzielenia przez 0')
except KeyboardInterrupt:
    print('Błąd przerwania')
except:
    print('Nie znany błąd')
finally:
    print('Koniec!')


