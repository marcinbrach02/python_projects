
def sum(a, *args):
    for v in args:
        a += v
    return a


print(sum(2))
print(sum(2, 3))
print(sum(2, 3, 4))

tab = [4, 5, 7]
# 2, *tab -> 2, tab[0], tab[1], tab[2]
print(sum(10, *tab))  # * - kolejne argumenty tablicy przekazane za do funkcji - rozpakowanie tablicy

print(*tab)



