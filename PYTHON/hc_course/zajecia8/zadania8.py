# ad1
# print([x**x for x in [1,2,3,4]])
# print([x/2 if x%2 else "Nope" for x in range(10,16)])


# ad2
#a
# my_list = [x**3 for x in range(1,11)]
# print(my_list)
#b
# my_list = [ord(i) for i in "Marcin"]
# print(my_list)
#c
# import math
# my_list = [math.sin(math.radians(x)) for x in range(0,361,10)]
# print(my_list)
#d
# my_list = [len(x) for x in ["Ania", "Mateusz", "Tomasz", "Dawid", "Agata"]]
# print(my_list)
#e
# my_list = [2*x for x in range(100) if x%3==0 and 2*x < 100]
# print(my_list)
#f
# import random
# my_list = [random.random() if x%2 else -(random.random()) for x in range(100)]
# print(my_list)


# ad3
#a
# import matplotlib.pyplot as plt
# X = [x+1 for x in range(-10,10)]
# Y = [2*x+5 for x in X]
# plt.axhline()
# plt.axvline()
# plt.plot(X,Y,'r-')
# plt.xlabel("Oś OX")
# plt.ylabel("Oś OY")
# plt.title("Wykres funkcji y=2x+5")
# plt.show()

#b
# import matplotlib.pyplot as plt
# X = [x+1 for x in range(-10,10)]
# Y = [x**2-2*x-8 for x in X]
# plt.axhline()
# plt.axvline()
# plt.plot(X,Y,'b-')
# plt.xlabel("Oś OX")
# plt.ylabel("Oś OY")
# plt.title("Wykres funkcji y=x^2-2x-8")
# plt.show()

#c
# import matplotlib.pyplot as plt
# import math
# X = [x for x in range(0,361,10)]
# Y = [math.sin(math.radians(x)) for x in X]
# plt.axhline()
# plt.axvline()
# plt.plot(X,Y,'k-')
# plt.xlabel("Oś OX")
# plt.ylabel("Oś OY")
# plt.title("Wykres funkcji sinus")
# plt.show()

#d
# import matplotlib.pyplot as plt
# import random
# X = [x+1 for x in range(100)]
# Y = [random.random() if x%2 else -(random.random()) for x in X]
# plt.axhline()
# plt.axvline()
# plt.plot(X,Y,'k-')
# plt.show()


# ad4
# import matplotlib.pyplot as plt
# tasks = {"Praca": 8, "Sen": 8, "Posiłek": 2, "Relax": 2, "Oglądanie TV": 1, "Zakupy": 1, "Kino": 2}
# plt.title("Zadanie 4")
# plt.pie(tasks.values(), labels=tasks.keys(), autopct="%.0f %%")
# plt.show()


# ad5
# import matplotlib.pyplot as plt
# import random
# X = [x for x in range(100, 10000, 10)]
# Y = [-50 + random.choice((-1,1)) * random.random() for x in X]

# plt.title("Zadanie 5")
# plt.plot(X, Y,'b--')
# plt.ylim(-100,0)
# plt.xlim(100, 10000)
# plt.xscale("log")
# plt.show()
