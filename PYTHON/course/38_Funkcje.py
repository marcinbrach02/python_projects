
c = 10


def f1(a, b = c):
    return a + b + c

#f1(1, 2)

print(f1(2))

#Źle - lista jest tworzona tylko raz!
# def addtolist(element, list=[]):
#     list.append(element)
#     return list
#
#
# l = ['a', 'b', 'c']
#
# print(addtolist('d', l))
# print(addtolist('a'))
# print(addtolist('b'))
# print(addtolist('c'))


#Ok lista jest tworzona jesli jest None
# def addtolist(element, list=None):
#     if list is None:
#         list = []
#     list.append(element)
#     return list
#
# l = ['a', 'b', 'c']
#
# print(addtolist('d', l))
# print(addtolist('a'))
# print(addtolist('b'))
# print(addtolist('c'))


#Ok  #REST - doc stringi
def addtolist(element: str, list: list=None) ->list:
    """
    Dodaje element do listy
    :param element: Łańcuch
    :param list: Dowolne lista
    :return: Lista z Elementem
    """
    if list is None:
        list = []
    list.append(element)
    return list

l = ['a', 'b', 'c']

print(addtolist('d', l))
print(addtolist('a'))
print(addtolist('b'))
print(addtolist('c'))
print(addtolist(12))

print(addtolist.__doc__)
print(addtolist.__annotations__)






