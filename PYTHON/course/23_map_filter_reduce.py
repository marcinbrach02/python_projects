from functools import reduce


def test(a):
    return a * 2


test = lambda a: a * 2


print(test)
print(type(test))

l = [
    (2, 3),
    (4, 2)
]

l.sort(key=lambda e: e[1])
print(l)

l2 = [2, 3, 4, 5, 6, 7, 8]
p = map(lambda a: a**2, l2)

print(p)

for v in p:
    print(v)

evalues = list(filter(lambda x: x % 2 == 0, range(0, 1000)))
print(evalues)

strings = [
    'add',
    'delete',
    'ss',
    'aa'
]

strings = list(filter(lambda s: len(s) >= 3, map(lambda s: s.strip(), strings)))

print(strings)

print(reduce(lambda x, y: x ** y, range(2, 10)))

p = [e**2 for e in range(1, 100) if e % 2 == 0]
print(p)












