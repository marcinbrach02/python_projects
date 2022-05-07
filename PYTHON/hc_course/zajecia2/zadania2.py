# ad1
age = int(input("Ile masz lat?\n"))
print("Wspaniale! Teraz masz: " + str(age))
age=age+1
print("Za rok będziesz miał: " + str(age))

# ad2
x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj druga liczbę: "))

print("Suma wynosi: " + str(x+y))
print("Różnica wynosi: " + str(x-y))
print("Iloczyn wynosi: " + str(x*y))

if y!=0:
    print("Iloraz wynosi: " + str(x/y))
else:
    print("Dzielenie przez zero jest niemożliwe!")

# ad3
number = float(input("Podaj liczbę: "))

if (number % 2) == 0:
    print("Liczba jest parzysta!")
else:
    print("Liczba jest nieparzysta!")

# ad4
age = int(input("Podaj wiek: "))
money = float(input("Podaj ilość pieniędzy w portfelu: "))

if age < 18 and money < 20:
    print("Jesteś niepełnoleti i nie masz wystarczająco dużo pieniędzy!")
elif age < 18 and money >= 20:
    print("Jesteś niepełnoleti ale masz wystarczającą ilość pieniędzy!")
elif age >= 18 and money < 20:
    print("Jesteś pełnoleti i nie masz wystarczająco dużo pieniędzy!")
elif age >= 18 and money >= 20:
    print("Jesteś pełnoleti i masz wystarczającą ilość pieniędzy!")

# ad5
val = 10/3 # należy uzyć 10//3 lub 10%3 aby otrzymać pozostałe wyniki
if val > 3:
    print("big")
elif val == 3:
    print("middle")
else:
    print("small")

# ad 6
wybor = int(input("Czy chcesz obliczyć dochód miesięczny czy roczny? \n 1 - miesięczny, 2 -roczny \n"))

if wybor == 1:
    dochod = float(input("Podaj dochód miesięczny: "))
    dochod = dochod * 12
    print("Dochód roczny wynosi: " + str(dochod))
elif wybor == 2:
    dochod = float(input("Podaj dochód roczny: "))
    print("Dochód roczny wynosi: " + str(dochod))

if dochod > 120000:
    print("Podatek dochodowy wynosi: " + str(dochod*0.32))
elif dochod <= 120000:
    print("Podatek dochodowy wynosi: " + str(dochod*0.17))
