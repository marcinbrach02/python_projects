
l1 = [(x ** 2, x * 2) for x in range(1, 100)]

print(l1)

l2 = [
    (2, 4),
    (5, 6)
]


l3 = [komorka * 2 for wiersz in l2 for komorka in wiersz]
print(l3)





