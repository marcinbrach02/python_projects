# ad1
# def compare(a,b,c):
#     if a > b and b < c:
#         return 3
#     elif a < b and c == 3:
#         return 5
#     elif a <= b and c > 1:
#         return 10
#     else:
#         return 99

# print(compare(3,1,2))
# print(compare(3,2,1))
# print(compare(3,3,3))
# print(compare(1,2,3))
# print(compare(3,2,3))
# print(compare(1,1,1))


# ad2
# def dodaj(a,b,c):
#     return a+b+c

# print(dodaj(1,2,3))


# ad3
# w cwiczeniach


# ad4
# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     return a/b

# while True:
#     sign = input("Jaką operacje chcesz wykonać? (+,-,*,/) ")
#     if sign == "+" or sign == "-" or sign == "*" or sign == "/":
#         break
#     else:
#         print("Podaj właściwą operację: ")
#         print("+ -> dodawanie, - -> odejmowanie, * -> mnożenie, / -> dzielenie")

# while True:
#     a = input("Podaj pierwszy argument: ")
#     b = input("Podaj drugi argument: ")
#     if a.isnumeric() == True and b.isnumeric() == True:
#         break
#     else:
#         print("Podaj liczbę!")

# a = int(a)
# b = int(b)

# if sign == "+":
#     print(add(a,b))
# elif sign == "-":
#     print(subtract(a,b))
# elif sign == "*":
#     print(multiply(a,b))
# elif sign == "+":
#     print(divide(a,b))
# else:
#     print("Wybrano błędną operację!")


# ad5
# def gender(name):
#     lenght = len(name)
#     if name[lenght-1] == "a":
#         return "kobieta"
#     else:
#         return "mężczyzna"

# names = ["Marcin", "Ania", "Kazimierz", "Małgorzata", "Tomasz"]
# names_items = {}

# for name in names:
#     my_gender = gender(name)
#     names_items.update({name : my_gender} )

# for key,value in names_items.items():
#     print(key + " : " + value)


# ad6
import math

def trapezoid_area(a,b,h):
    if isinstance(a, float) == True and isinstance(b, float) == True and isinstance(c, float) == True:
        return ((a+b)*h/2)
    else:
        return -1

def triangle_area(a,b,c):
    if isinstance(a, float) == True and isinstance(b, float) == True and isinstance(c, float) == True:
        half_area = (a+b+c)/2
        return math.sqrt(half_area*(half_area-a)*(half_area-b)*(half_area-c))
    else:
        return -1

def square_rots(a,b,c):
    delta = (b**2) - (4*a*c)
    if delta > 0:
        x1 = (-1 * b - math.sqrt(delta)) / (2*a)
        x2 = (-1 * b + math.sqrt(delta)) / (2*a)
        return x1,x2 #dobrze?????
    elif delta == 0:
        return (-1*b) / (2*a)
    elif delta < 0:
        print("Brak pierwiastków rzeczywistych!")



def load_data(a,b,c):
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))



# case = int(input("Wybierz co chcesz obliczyć: \n1-pole trapezu, 2-pole trójkata, 3-pierwiastki równania kwadratowego"))

# if case == 1:


#print(isinstance(3.0, float))

print(triangle_area(2,2,3.0))

#dokończyć!!!!


