# pętla for
# tab = [1,2,3,4,5]

# for element in tab:
#     print(element)

# for element in [1,2,3,4,5]:
#     print(element)

# cw1
# names = ["Marcin", "Paweł", "Przemek", "Weronika"]
# for name in names:
#     print(name)

# cw2
# numbers = [1,5,10,15,20]
# for i in numbers:
#     print(i**2)
# print("to jest po za petla")

# generator range
# for i in range(5):
#     print(i)

# for i in range(2,8):
#     print(i)

# for i in range(2,10,3): # zakres z krokiem
#     print(i)

# cw3
# for i in range(20,101):
#     print(i)

# petla while
# value = 5
# while value <= 10:
#     print(value)
#     value = value + 1 #zmniejszenie licznika value


# while True:
#     print("spam")


# val = 0
# while val < 1000:
#     print(val)
#     val = val + 2
#     if (val == 10):
#         print("Już mi się nie chce")
#         break



# cw4
# value = 100
# while True:
#     value = value + 5
#     print(value)
#     if (value == 1000):
#         break

# for + if

# for a in range(0, 100):
#     print(a)
#     if (a < 10):
#         print("To mała liczba")
#     elif (a == 30):
#         print("Dobra, starczy!")
#         break


# continue
# for a in range(0, 10):
#     print("hej")
#     if(a==2) or (a==5):
#         continue
#     print(a)


# cw5
# for a in range(0, 101):
#     if (a % 3 == 0) or (a % 5 == 0):
#         continue
#     print(a**2)

# zastosowanie w słownikach
# my_dict = {"a" : "ananas", "b": "cucumber"}
# for key in my_dict.keys():
#     print(key, my_dict[key])
# print(my_dict.items())


#krotki tuple

#sety
# my_set = {1,10,100,1000}
# for element in my_set:
#     print(element)


# for x in range(0,8):
#     for y in range(0,6):
#         print("Pixel: " + str(x) + ", " + str(y))
#         if y == 2:
#             print("Tu stoi przeszkoda")


# for x in range(0,8):
#     for y in range(0,6):
#         for z in range(0,5):
#             print("Pixel: " + str(x) + ", " + str(y) + ", " + str(z))
#         if y == 2:
#             print("Tu stoi przeszkoda")


# domyslnie funkcja print przechodzi do nowej linii
# print("hahaha")
# print("hehehe", end="")
# print("hihihi")


# cw7
#sposób nr 1
# for y in range(5):
#     for x in range(6):
#         if (x == 0 and y==1) or(x == 2 and y==3) or (x == 2 and y==4) or (x == 3 and y==4):
#             print("X ", end="")
#         elif (x == 1 and y==1) or(x == 2 and y==0) or (x == 3 and y==3) or(x == 5 and y==3):
#             print("* ", end="")
#         elif (y==2):
#             print("= ", end="")
#         else:
#             print(". ", end="")
#     print(" \n")


# sposób nr 2
row1=[".",".","*",".",".","."]
row2=["X","*",".",".",".","."]
row3=["=","=","=","=","=","="]
row4=[".",".","X","*",".","*"]
row5=[".",".","X","X",".","."]
colums = [row1, row2, row3, row4, row5]
for element in colums:
    print("".join(element)) # funkcja join zeby nie wyswietlic z listy








