#import modul1

#from modul1 import f1 as f3, pi
# from math import pi  #kolejnosc importó ma również znaczenie


# KOlejność przeszukiwania modułów:
# ./
# %PYTHONPATH%
# Python install dir

from modul1 import pi
from modul1 import * #wrzucenie wszystkiego do przestrzenie nazw - nalezy unikac


def f1():       #jedna funkcja nadpisała drugą
    from math import pi     #import tylko wewnatrz funkcji
    print(pi)


f1()  # uzycie bez nazwy modul1
#f3()
print(pi)


# print(modul1.STALA)





