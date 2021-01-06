from random import randint


# def randoms(i, *args):
#     liczby = [ random.randint(1, 100) for value in range(1, i)]
#     return liczby


def randoms(count, *without):
    l = []
    while len(l) < count:
        r = randint(1, 1000)
        if r not in without:
            l.append(r)
    return l


def gen_randoms(count, *without):
    i = 0
    while i < count:
        r = randint(1, 1000)
        if r not in without:
            i += 1
            yield r


print(randoms(10, 2, 4))
print(list(gen_randoms(50, 1, 30)))
print(randoms(10))
tab = [3, 4, 5]
print(randoms(22, *tab))






