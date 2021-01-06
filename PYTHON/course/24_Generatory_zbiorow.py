
baza = [2, 3, 4, 5, 6]

nowa_baza = []

for liczba in baza:
    if liczba % 2 == 0:
        nowa_baza.append(liczba ** 2)

print(nowa_baza)

nowa_baza = list(filter(lambda liczba: liczba % 2 == 0, map(lambda liczba: liczba ** 2, baza)))

print(nowa_baza)


nowa_baza = [liczba ** 2 for liczba in baza if liczba % 2 == 0]


print(nowa_baza)







