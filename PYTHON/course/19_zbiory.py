from operator import itemgetter, attrgetter

l = [
    ('b', 5),
    ('a', 4),
    ('c', 1)
]

# def getElementToSort(element):
#     return element[1]
#
# l.sort(key=getElementToSort)

#attrgetter('pole')

l.sort(key=itemgetter(1), reverse=True)


print(l)




