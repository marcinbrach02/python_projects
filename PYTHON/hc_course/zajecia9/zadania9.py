# ad1
##wąż
# class Snake():
#     name = ""
#     age = 0
#     size = 0

#     def name(self):
#         print(self.name)

#     def sound(self):
#         return "s"*4

#     def move(self, size):
#         return


# boa = Snake()
# boa.name = "BOA"


# boa.sound()



##lodówka

# class Fridge():
#     capacity = 0
#     power = 0
#     colour = ""

#     def frost_time(self):
#         return self.capacity/power
#         def temperature(self):
#             return temperature


# amica = Fridge()
# amica.capacity = 80
# amica.power = 8












# ad2
##a
# class Turtle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#         self.x = 0

#     def say_name(self):
#         print("Hi I am turtle " + self.name)

#     def move(self):
#         self.x = self.x + self.speed

#     def get_position(self):
#         return self.x


# ninja = Turtle("Donatello", 5)
# ninja.say_name()
# ninja.move()
# ninja.move()
# ninja.move()
# x = ninja.get_position()
# print(x)


##b
# class Book:
#     def __init__(self, author, title, pages):
#         self.author = author
#         self.title = title
#         self.pages = pages
#         self.current_page = 0

#     def print_book(self):
#         print(self.title + " written by " + self.author + " has " + str(self.pages) + " pages")

#     def goto_page(self, page):
#         if page < self.pages:
#             self.current_page = page
#         else:
#             self.current_page = self.pages

#     def get_current_page(self):
#         return self.current_page


# book = Book("Mróz", "Przepaść", 560)
# book.print_book()
# book.goto_page(432)
# x = book.get_current_page()
# print(x)
# book.goto_page(201)
# x = book.get_current_page()
# print(x)


# ad3
# class Human:
#     def __init__(self, name, surname, age, money, position):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.money = money
#         self.position = position

#     def introduce(self):
#         print("Hi I am " + self.name + " " + self.surname)

#     def move(self, distance):
#         self.position = self.position + distance

#     def get_position(self):
#         return self.position

#     def get_money(self):
#         return self.money

#     def say_something(self, something):
#         print(something)

#     def payment(self, salary):
#         self.money = self.money + salary

#     def can_buy_beer(self, count, price):
#         if self.age >= 18 and self.money >= count * price:
#             return True
#         else:
#             return False

#     def buy_beer(self, count, price):
#         if self.can_buy_beer(count, price):
#             self.money = self.money - count * price
#             print("Great! "+self.name+" bought "+str(count)+" beers!")
#         else:
#             print("Not possible for this human!")

## nazwa klasy: Human
## pola: name, surname, age, money, position
## metody: introduce, move, get_position, get_money, say_something, payment, can_buy_beer, buy_beer
## stworzenie metody:
# me = Human("Marcin", "Brach", 34, 10, "tester")

## zakup jednego piwa za 6 zł ze sprawdzeniem czy mmam na tyle
# if me.can_buy_beer(1, 6) == True:
#     me.buy_beer(1, 6)

## zarobienie 5000
# me.payment(5000)




# ad4
#a
class Bird():
    def __init__():
        pass

    def size():






















