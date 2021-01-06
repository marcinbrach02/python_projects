
# class UserData:
#     pass            #nie mozemy okreslac wlasciwosci mozemy jedynie okreslac nazwy metod

class UserData:

    def __init__(self, fname: str, lname: str):             #konstruktor uruchamiany podczas tworzenia obiektu
        print('uruchomienie')
        self.__fname = ''

    def __del__(self):                                      #destruktor uruchomienie podczas usuwania obiektu - gwarancja wywolania
        print('test destruktora')

    def __str__(self):
        print(self.get_fname())

    def set_fname(self, fname: str):
        if len(fname) >= 3:
            self.__fname = fname        # __ - zmienna prywatna private

    def get_fname(self):
        return self.__fname


u = UserData('dd', 'ddd')      #uzycie parametrow do konstruktora

#u.fname = 'test'

u.set_fname('test')
u.__fname = 'dddd'

print(u.__fname)
print(u.get_fname())
print(u.__dict__)
#print(u)









