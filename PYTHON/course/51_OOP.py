import json
from abc import ABC


class User(ABC):                                        #klasa abstrakcyjna abstract base class - ABC
    def __init__(self, fname: str, lname: str ):
        self.__fname = fname
        self.__lname = lname
        print('Konstruktor klasy User')
        if (type(self) == User):
            raise Exception('Abstract')

    @property
    def fname(self):
        return self.__fname

    def show(self):
        print('Imię: {}'.format(self.__fname))

# class Client(User):                                      #dziedziczenie z klasy User mozna po wielu po przecinku
    # def __init__(self, client_no: int):                     #przy tworzeniu obiektu konstruktor jest przysłaniany
    #     self.__client_no = client_no
    #     print('Konstruktor klasy Client')


class ToJson:
    def as_json(self):
        return json.dumps(self.__dict__)

    def show(self):
        print('Show z ToJson')


class Client(ToJson, User):
    def __init__(self, fname: str, lname: str, client_no: int):
        super().__init__(fname, lname)
        self.__client_no = client_no

    def show(self):
        #super().show()
        User.show(self)
        print('Numer: {}'.format(self.__client_no))


#u = User('Krzysiek', 'm')
c = Client('Krzysiek', 'M', 222)
c.show()
print(c.as_json())

#print(isinstance(u, User))
print(isinstance(c, User))

# if isinstance(u, User):
#     print(u.show())
# if isinstance(c, User):
#     print(c.show())
#


