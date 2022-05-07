# funkcje np. print(), input()
# składnia funkcji
# def nazwa_funkcji(zero lub więcej parametró):
#     instrukcje do wykonania(ciało funkcji)

#funkcja dodająca dwie wartości
# def add(a, b):
#     print(a+b)

# add(5,6)
# add(-6,-7)
# add(12.5,36.6)
# add("Hard", "Coder")

# funkcja na pole prostokata
# def calkulate_area(a, b):
#     print(a*b)

# calkulate_area(3,5)

# funkcja do dzielenia liczb i sprawdzenia wartości
# def divide(a, b):
#     if b!=0:
#         print(a/b)
#     else:
#         print("Don't do that")

# divide(10,3)
# divide(10,0)
# divide(9,5)

# funkcja na pole koła
# def circle_area(r):
#     if r>0:
#         print(3.14*r**2)
#     else:
#         print("Don't do that")


# circle_area(4)
# circle_area(-4)
# circle_area(0)

# def trapezoid_area(a, b, h):
#     if a>0 and b>0 and h>0:
#         print( (a+b)*h / 2 )
#     else:
#         print("To niemożliwe")


# trapezoid_area(1,2,3)
# trapezoid_area(-1,2,3) # tego nie policzy bo nie spełnia warunku

#!!!!! dokonczyc !!!!!
# def is_grather_than_zero(x):
#     if x>0:
#         print(str(x) + " jest większe od 0")
#     elif x==0:
#         print(str(x) + " jest równa 0")

# is_grather_than_zero(5)
# is_grather_than_zero(0)


# def annual_earnings(salary):
#     return 0.7*salary*12

# money202 = annual_earnings(5000)
# print(money202)

#print(annual_earnings(5000)) tak tez można wyswietlac

# !!! o co kaman??
# def bmi_factor(hight, weight):
#     return weight/(hight**2)

# def translate_bmi():
#     if x >= 25:
#         return "Nadwaga"
#     elif x>18.5:
#         return "Optimum"
#     else:
#         return "Niedowaga"


# print( translate_bmi(bmi_factor(1.76,75)) )



# def zw():
#     print("Triangle area: ")
#     a = input("Give a: ")
#     h = input("")
# błąd przy mnozeniu stringów


#funkcja powinna zawsze zwracać! w kazym ifie

# x = print(7)
# print(x) # print zwraca None


# def say(name, count = 2): #wartosc domyslana jesli nie wpiszemy parametrów
#     for i in range(count):
#         print(name)

# say("Marcin", 2)

# say("Marcin", 5)



# def divide(a, b):
#     if b:
#         return a/b

# print(divide(5, 2))
# print(divide(a=5, b=2))
# print(divide(b=2.5, a=5)) #jesli inna kolejnosc musi byc podany parametr
# print(divide(2, b=5))

# zasiąg zmiennych
# y=5
# def fun(a,b):
#     x=a+b

# fun(2,4)
# print(y)
# print(x)
# a = fun(1,3)
# print(a)

# funkcja zwracająca wiele zmiennych
def fun(a,b,c):
    return (a**2,b**2,c**2)

x1,x2,x3 = fun(1, 2, 3)
print(x1, x2, x3)



