# budowanie klasy i obiektów
# class Rectangle:
#     a = 0
#     b = 0

#     def area(self):
#         return self.a * self.b

#     def perimeter(self):
#         return 2*self.a + 2*self.b

#     def print_name(self):
#         print("Prostokąt")

# rect = Rectangle() #stworzenie obiektu
## print(rect)  # wyświetlenie typu obiektu rect
# rect.a = 5      # ustawienie wartości pól
# rect.b = 10
# print(rect.a, rect.b)   # wyświetlenie wartości pól

## rect.c = 100        # minus pythona - pozwala na dodanie c do obiektu, operacja bezuzyteczna
## print(rect.c)

# x = rect.area()         # wykonanie matody na swoich self parametrach
# y = rect.perimeter()
# print(x, y)
# rect.print_name()

# rect1 = Rectangle()
# rect1.a = 10
# rect1.b = 99
# print(rect1.area(), rect1.perimeter())


# lista - obiekt klasy list
# my_list = list()    #stworzennie pustej listy
# print(type(my_list)) #wyświetlenie typu my_list
# my_list.append(2)   #wywołanie metody na obiekcie klasy list
# my_list.append(5)
# print(my_list)


# czas - obiekt klasy datetime
# import datetime
# x = datetime.datetime.now() #niejawne stworzenie obiektu
# print(type(x))              #wyświetlenie typu x
# print(x.hour)               #odwołanie do pola hour obiektu x
# print(x.minute)
# print(x.year)
# print(x.timestamp())        #wywołanie metody na obiekcie x


#konstruktor klasy
# class Rectangle:
#     def __init__(self, a, b):   #definicja konstruktora
#         self.a = a
#         self.b = b

#     def area(self):
#         return self.a * self.b

# rect = Rectangle(5, 10)     #konstruktor wymaga 2 argumentów
# print(rect.area())


# dziedziczenie
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is " + str(self.name) +
            " and I am " + str(self.age) + " years old")
    def sound(self):
        print("Default sound")

class Dog(Animal):          #klasa Dog dziedziczy z klasy Animal
    def sound(self):
        print("Woof Woof")

class Cat(Animal):
    def sound(self):
        print("Meow Meow")


python = Animal("Python", 30)   #stworzenie obiektu python i wywołanie na nim metod
python.introduce()
python.sound()

dog = Dog("Goldi", 2)           #stworzenia obiektu Dog który dziedziczy z klasy Animal
dog.introduce()
dog.sound()

cat = Cat("Mruczek", 5)
cat.introduce()
cat.sound()
