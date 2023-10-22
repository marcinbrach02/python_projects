#operacje na plikach
#my_file = open("D:\\demo.txt", "r") #z podaniem ściezki \\ bez nowej linii!
# my_file = open("demo.txt", "r")
# content = my_file.read()
# print(content)      #odczyt całego pliku


# my_file = open("demo.txt", "r")
# first_ten = my_file.read(10)
# second_ten= my_file.read(10)
# print(first_ten)
# print(second_ten)   # po odczytaniu ustawia kursor i jesli odczytasz cały to nie ma co odczytywac


# my_file = open("demo.txt", "r")
# for i in range(3):
#     print(my_file.readline())


# my_file = open("demo.txt", "r")
# tab = my_file.readlines()
# my_file.close()
# print(tab)
# print(tab[0]) #zapis linii do tablicy


# składnia with as

# with open("demo.txt", "r") as my_file:      #po wyjsciu z with plik jest zamykany bardziej "pajtonik" XD
#     first_ten = my_file.read(10)
#     print(my_file.read(15))

# print(first_ten)


# with open("demo_w.txt", "w") as f:
#     f.write("To jest pierwsza linia\n")     #przejscie do nowej linni jest konieczne
#     f.write("a to druga")


# with open("demo_w.txt", "a") as f:      #modyfikacja pliku tworzy jesli nie ma
#     f.write("\njest nowelą")


# with open("demo_w.txt", "r") as f:
#     print(f.read())


# cw1
# tab = ["Marcin", "Przemek", "Sylwia", "Szymon", "Emilia"]

# with open("names.txt", "w") as my_file:
#     for name in tab:
#         my_file.write(name + " " + str(len(name)) + "\n")


# with open("names.txt", "r") as my_file:
#     lines = my_file.readlines()
#     names = []
#     numbers = []
#     for line in lines:
#         name, number = line.split()
#         names.append(name)
#         numbers.append(int(number))


# print(names)
# print(numbers)

# try:
#     with open("dzisiaj.txt", "r") as f:         #w try except linijki po wcięciach
#         print(f.read())

# except FileNotFoundError:
#     print("Plik nie istnieje")

# except:
#     print("Błąd")

# try:
#     print(5/2)
#     print(10/5)
#     print(1/0)
#     print(5/5)
# except ZeroDivisionError:
#     print("Nie można dzielic przez zero")   #w linijce z exceptionem przerwie program dlatego napez kazda linijke


# try:
#     with open("new_file", "r") as f:
#         print(f.read())

# except FileNotFoundError:
#     print("Plik nie istnieje i/lub nie ma praw dostepu")
# except ValueError:
#     print("Coś z wartościami")
# except:
#     print("Dowolny inny błąd")


# try:
#     with open("new_file", "r") as f:
#         print(f.read())

# except FileNotFoundError:
#     print("Plik nie istnieje i/lub nie ma praw dostepu")
# finally:
#     print("Instrukcja z bloku finally")

# jakiez zadanie na filmie ekrutacyjne

# cw2
# try:
#     x = float(input("Podaj liczbe: "))
# except ValueError:
#     x=0

# print(x**2)


###

# def is_number(x):
#     try:
#         x = float(x)
#         return True
#     except ValueError:
#         return False

# x = input("Podaj liczbę: ")
# if is_number(x):
#     print(x**2)



#rzucanie wyjątków
def square_area(a):
    if a<=0:
        raise ValueError            #do rzucenia wyjątków służy raise
    return a*a

print(square_area(5))

print(square_area(-5))











