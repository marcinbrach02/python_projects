# Przykłady list comprehension

# lista 6 liczb
# my_list = []
# for index in range(6):
#     my_list.append(index+1)
# print(my_list)

# my_list2 = [index+1 for index in range(6)]
# print(my_list2)


# lista kwadratów 10 kolejnych liczb
# my_list = []
# for i in range(10):
#         my_list.append(i*i)
# print(my_list)

# my_list2 = [i*i for i in range(10)]
# print(my_list2)


# lista kwadratów liczb parzystych
# my_list = []
# for i in range(10):
#     if(i%2==0):
#         my_list.append(i*i)
# print(my_list)

# my_list2 = [i*i for i in range(10) if i%2==0]
# print(my_list2)


# lista kwadratów liczb parzystych lub zera
# my_list = []
# for i in range(10):
#     if(i%2==0):
#         my_list.append(i*i)
#     else:
#         my_list.append(0)
# print(my_list)

# my_list2 = [i*i if i%2==0 else 0 for i in range(10)]
# print(my_list2)


# cw1
# my_list = []
# for a in [8,10,15,19,25]:
#     if(a//3 >=5):
#         my_list.append(a+2)
# print(my_list)

# my_list2 = [a+2 for a in [8,10,15,19,25] if a//3>=5]
# print(my_list2)


# cw2
# my_list = [-i*i if i%2==1 else "haha" for i in range(5,21)]
# print(my_list)


# Moduł pyplot
# import matplotlib.pyplot as plt

# numbers = [5,10,15,3,20]
# plt.plot(numbers)

# argumenty plot po przecinku: kolor, sympol punktu, linia przerywana/kropki np:
# plt.plot(numbers, 'o')  #niepołączone punkty
# plt.plot(numbers, '.')  #niepołączone kropki
# plt.plot(numbers, 's')  #niepołączone kwadraty
# plt.plot(numbers, 'ro') #czerwone punkty
# plt.plot(numbers, 'g^') #zielone trójkaty
# plt.plot(numbers, 'k*') #czarne gwiazdki
# plt.plot(numbers, 'r-') #punkty połaczone czerwonymi liniami
# plt.plot(numbers, 'bD:') #niebieskie diamenty połaczone kropkami
# plt.plot(numbers, 'mp--')   #różowe pięciokąty połaczone przerywanymi liniami
# plt.show()


# Wykres funkcji y=5x-2
# import matplotlib.pyplot as plt

# X = [i+1 for i in range(0,10)]
# Y = [5*i - 2 for i in X]
# print(X)
# print(Y)

# plt.plot(X,Y, 'ro-')
# plt.show()


# Wykresy funkcji y=5x-2, y2 = -2x+5, y3=3x+3
# import matplotlib.pyplot as plt
# X = [x+1 for x in range(-10,10)]
# Y = [5*x-2 for x in X]
# Y2 = [-2*x+5 for x in X]
# Y3 = [3*x+3 for x in X]

# plt.axhline()   #linia pozioma osi
# plt.axvline()   #linia pionowa osi

# plt.plot(X,Y, 'ro-', X,Y2, 'b^-', X,Y3, 'gs-') #plot dla kilku funkcji na raz (tracimy na czytelności)

# opisy osi i labelka
# plt.xlabel("Oś OX")
# plt.ylabel("Oś OY")
# plt.title("Wykresy funkcji")
# plt.show()


# Wykres słupkowy
# import matplotlib.pyplot as plt
# import random

# names = ["Michał", "Szymon", "Emilia", "Paulina", "Rudolf"]
# ages = [random.randint(18,35) for name in names]

# plt.bar(names,ages, color = ["red", "green", "blue"])
# znaczniki osi x i y
# plt.xticks(names)
# plt.yticks(ages)
# plt.show()


# Wykres kołowy(pie chart)
# import matplotlib.pyplot as plt

# expenses = ["mieszkanie", "media", "jedzenie", "rozrywka", "nauka", "inwestycje"]
# values = [3000, 400, 1200, 300, 400, 1000]

# explode = [0 for i in expenses]
# print(explode)
# explode [expenses.index("inwestycje")] = 0.1
# print(explode)

# plt.pie(values, labels = expenses, explode = explode, autopct = "%.2f %%", shadow = True)
# plt.show()


# Klika wykresów w jednym oknie(subplot)
# import matplotlib.pyplot as plt
# import random, math

# X = [x for x in range(0,360+1,10)]
# Y1 = [math.cos(math.radians(i)) for i in X]
# Y2 = [random.random() for i in X]

# plt.subplot(2,1,1) #poziomy, poiny, index
# plt.plot(X,Y1, "r.-")
# plt.subplot(2,1,2)
# plt.plot(X,Y2, "bs:")
# plt.show()
