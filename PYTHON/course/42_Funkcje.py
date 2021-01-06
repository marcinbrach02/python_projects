from random import randint


def f1(v, x = 1, y = 2):
    pass


# print(f1(10, 2, 4))
# print(f1(10, y=2, x=3)) #mozliwosc zamiany parametrow przy wywolaniu
# print(f1(12, y=3)) #mozliwe jest wywolanie mniejszej liczby argumentow
# print(f1(v=2, y=3)) #wszystkie parametry wywołane przez nazwę
# print(f1(y=3, v=2))

def gen_randoms_without(*without, count, min=0, max=10 ):
    i = 0
    while i < count:
        r = randint(min, max)
        if r not in without:
            i += 1
            yield r

print(list(gen_randoms_without(3, 4, 6, 3, count=50, min=0, max=30))) #argumenty pozycyjne na poczatku wywołania
print(list(gen_randoms_without(count=10, min=0, max=30)))

print(3, 4, 5, 5, sep=',', end='\t')








