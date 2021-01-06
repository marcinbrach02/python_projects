import random

def suma(a, b):
    if a == 1:
        return
    return a + b


print(suma(2, 2))
print(suma(1, 2))


def multi():
    yield 1
    yield 2
    yield 3


# print(multi())
# print(multi())
# print(multi())

for value in multi():
    print(value)

def generate_randoms(i):
    return [random.randint(0, 1000) for value in range(1, i)]

def generate_random(i):
    for v in range(1, i):
        yield random.randint(0, 1000)


for value in generate_randoms(100):
    print(value)




