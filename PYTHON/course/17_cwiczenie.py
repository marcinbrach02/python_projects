
plik = open('words.txt', encoding='utf-8')

b = set(plik)

zm = 0
for linia in b:
    if len(linia.strip()) > 3:
            zm += 1

print(zm)


