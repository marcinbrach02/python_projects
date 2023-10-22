# import random
# print(random.randint(0,100)) #losuje liczbę z zakresu 0 do 100
# print(random.random()) #losuje liczbę z zakresu 0.0 do 1.0
# random.choice(tab) #zwraaca losowy element z listy tab

# cw 1
# print(random.randint(1,23)) #losuje liczbę z zakresu 0 do 23

# cw2
# years = [1988, 1999, 2002, 1995, 1960, 1993]
# print(random.choice(years))

# cw3
# values = range(1, 50)
# print(random.sample(values, 6)) #wygenerowanie sześciu kul

# import math
# print(math.sqrt(4))
# print(math.pow(2,10))

# cw4
# print(math.sqrt(81))
# print(math.pow(8, 10))
# print(math.sqrt(2) + math.sqrt(3) + math.sqrt(6))

#print(math.sqrt(-5))

# cw5
# print(math.pow(125, (1/3))) #pierwiastek to potęga do 1/3


# print(math.floor(5.5)) # podłoga z 5.5
# print(math.ceil(5.5)) # sufit z 5.5
# print(math.trunc(5.5)) # usunięcie częsci ułamkowej z N

# print(math.pi) #liczba pi


# cw6
# numbers = [10.5, 123.3, 0.95, math.pi]

# for number in numbers:
#     print(number, math.floor(number), math.ceil(number), math.trunc(number))


# print(math.sin(math.radians(90))) # dla funkcji sin nalezy podać w radianach
# print(math.sin(90*math.pi/180)) # to samo co wyżej

# print(math.log(2,10))
# print(math.log10(1000))
# print(math.e)


#time.sleep(3)

# cw7
# import time
# seconds = int(input("Podaj liczbę sekund: "))
# while seconds!=0:
#     print(seconds)
#     time.sleep(1)
#     seconds = seconds - 1


# seconds = int(input("Podaj liczbę sekund: "))
# for i in range(seconds, 0, -1):         # do 0 z krokiem -1
#     print(i)
#     time.sleep(1)
#     seconds = seconds - 1


# print(time.localtime())
# now = time.localtime()
# print(time.strftime("%H : %M : %S" ,now))

# print(time.time()) # liczba sekund od 1 stycznia 1970

# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.today())
# print(datetime.date.today())
# print(datetime.date.today().year)

# d1 = datetime.date(2020, 5, 18)
# print(d1)
# d2 = datetime.date(year = 2021, month = 5, day = 25) #jawne parametry
# print(d2)

# delta = d2 - d1
# print(delta)

# d3 = d2 + datetime.timedelta(days = 40)
# print(d3)


# import keyword

#print(keyword.kwlist) # wyswietlenie słów kluczowych w pythonie

# words = ["for", "print", "break"]
# for word in words:
#     print(word, end="")
#     if keyword.iskeyword(word):
#         print(" is keyword in Python")
#     else:
#         print(" is not keyword in Python")


# import math as majca
# print(majca.sqrt(4))


# from datetime import date # z mpdułu datetime importuje submoduł date
# print(date.today())


# import time
# print(dir(time))

# import time, math, random, keyword

# for i in time, math, random, keyword, list, tuple:
#     print("Functions in " + str(i))
#     print(dir(i))


import random
my_list = [1,2,3]
random.shuffle(my_list)
print(my_list)













