# ad1
#rozw w ćWiczeniach


# ad2
# import random, math

# start = int(input("Podaj początek zakresu: "))
# stop = int(input("Podaj koniec zakresu: "))

# numbers = ( random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop),
#             random.randint(start, stop))

#print(numbers)

# i=0
# result = 1
# while i<=9:
#     result = result * numbers[i]
#     i = i+1

# print(result)
# result = math.pow(result, (1/10))

# print("Średnia geometryczna wynosi: " + str(result))


# ad3
import math

def triangle_area(a,b,angle):
    return (a * b * math.sin(math.radians(angle)))/2

a = float(input("Podaj długość boku A: "))
b = float(input("Podaj długość boku B: "))
angle = int(input("Podaj kąt ostry pomiędzy bokiem A i B: "))

if a > 0 and b > 0 and angle > 0 and angle < 90:
    print("Pole trójkata wynosi: " + str(triangle_area(a,b,angle)))
else:
    print("Podane dane są nieprawidłowe dla trójkąta ostrokatnego")







