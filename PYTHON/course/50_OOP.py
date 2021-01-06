
class Test:
    c = 0                       #wlasciwosci statyczne
    def __init__(self):
        print(type(self).c)     #
        Test.c += 1             #dostep do zmiennej c (klasy statycznej)

    @staticmethod
    def get_counter():          #metoda bez selfa - metoda statyczna
        return Test.c

    @classmethod                #pod cls trafia klasa
    def get_counter2(cls):
        print(cls)
        return cls.c

    def __new__(cls, *args, **kwargs):
        print('test')

    def __init__(self):
        print(type(self).c)     #
        Test.c += 1
        print('test2')


t1 = Test()
t2 = Test()
t3 = Test()

# print(Test.get_counter())     #nazwa klasy i metoda do wywolania metody statycznej
# print(t3.get_counter())     #z uzyciem docoratora @staticmethod mozna wywolac metode statyczna z obiektu
# print(Test.get_counter2())
# print(t3.get_counter2())














