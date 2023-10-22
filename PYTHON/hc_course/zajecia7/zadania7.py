# ad1
# import random

# a = int(input("Podaj pierwszą liczbę z przedziału: "))
# b = int(input("Podaj drugą liczbę z przedziału: "))

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(a,b))

# print(numbers)

# with open("dane.txt", "w") as file:
#     for i in range(10):
#         for j in range(numbers[i]):
#             file.write("*")
#         file.write("\n")

# chars = []
# with open("dane.txt", "r") as file:
#     for i in range(10):
#         chars.append(file.readline())

# print(chars)

# for i in range(10):
#     chars[i] = chars[i].replace("*", ".")

# with open("dane.txt", "a") as file:
#     for i in range(10):
#         file.write(chars[i])

# print(chars)


# ad2
# import random
# names = ["Ania", "Mateusz", "Marcin", "Ola", "Natalia"]
# marks = ["2.0", "3.0", "3.5", "4.0", "4.5", "5.0"]

# rating_list = {}
# for name in names:
#     rating_list.update({name: random.choice(marks)})

# index=1
# with open("oceny.txt", "w") as file:
#     for key in rating_list.keys():
#         print(key, rating_list[key])
#         file.write(str(index) + ". " + key + ": " + rating_list[key] + "\n")
#         index =index+1

## enumerate() ??
## with open("oceny1.txt", "w") as file:
##     for key in enumerate(rating_list.items(), start=1):
##         print(key + str(rating_list[key]))
##         file.write(". " + key + ": " + rating_list[key] + "\n")


# ad3
# nie zrobiona walidacja kodu
# try:
#     code = input("Podaj kod pocztowy: ")

#     lines = []
#     with open("kody.csv", "r", encoding='UTF-8') as file:
#         for i in range(50000):
#             lines.append(file.readline())

#     line = []
#     for element in lines:
#         if element.startswith(code) == True:
#             line = element.split(";")

#     print("Podany kod jest z miasta: " + line[2])

# except IndexError:
#     print("Nie znaleziono podanego kodu!")

# ad4
#1
# try:
#     my_list = [1,2,3]
#     x = my_list[5]
# except IndexError:
#     print("Wystąpił błąd indexu - IndexError")
#2
# try:
#     my_dict = {"apples":3, "bananas":5, "oranges":9}
#     print(my_dict["cherries"])
# except KeyError:
#     print("Wystąpił błąd klucza - KeyError")
#3
# try:
#     print("Zmyslow" + 5)
# except TypeError:
#     print("Wystapił błąd typu danych - TypeError")
#4
# try:
#     import maths
# except ModuleNotFoundError:
#     print("Wystąpił błąd modułu - ModuleNotFoundError")
#5
# try:
#     x = 1
#     y = 2
#     z = w
# except NameError:
#     print("Wystąpił błąd definicji zmiennej - NameError")


#5

#!!!



















