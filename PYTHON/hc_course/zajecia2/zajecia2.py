# wyświetlanie zmiennych
x= 1991
y= 2020
print(x)
print(y)
print(y-x)

# wczytywanie danych do zmiennej i wyświetlanie go
print("Jak się nazywasz?")
name = input()
print(name)

print(input("Ile masz lat? "))
wiek = input("Podaj wiek: ")
print("Mam: " + wiek + " lat")

# wyświetlanie słow kluczowych języka Python
import keyword
print(keyword.kwlist)

#rzutowania wczytywanej zmiennej string na int lub float
# a = int(input("Podaj a: "))
a = input("Podaj a: ")
b = input("Podaj b: ")
h = input("Podaj h: ")
pole = ((float(a)+float(b))*float(h))/2
print("Pole trapezu o podstawach: a: " +a+ " b: " + b + " i wysokości h: " +h+ " wynosi:" + str(pole))

#wartosci logiczne
print(500>1000)
print(500<=500)
print(2+100<102)
print("napis"=="napis")
print("napis"=="Napis")
#print("a">"b"zzz) # błąd co to zzz?
print(500=="500")
#print(500<="500") # błąd niemozliwa nierówność int i str
print(100!="100")

# instrukcja warunkowa if
x = 5 # 3 lub mniej dla elsa
if x > 3:
    print("Lepiej mieć 5 zł niz 3zł")
else:
    print("Masz 3 zł")

#rzutowanie do inta i warunek
wiek = int(input("Podaj wiek: "))
if wiek >= 18:
    print("Tak możesz grać w Wiedźmina")
    print("Graj!")
elif wiek >= 16:
    print("Możesz jak rodzice sie zgodza")
else:
    print("Nie możesz!")

# kolejny przykład
x = int(input("Podaj dowona liczbę:"))
if x>0:
    print("Liczba dodatnia")
elif x<0:
    print("Liczba ujemna")
else:
    print("Zero")

#warunki logiczne
x = 4
y = 5
print(x > 1 and y > 1)
print(y < 10 and x > 10)
print(x > 1 or y > 1)
print(x > 1 or y > 10)
print(x > 2 and y <= 5 and x+y==9)
