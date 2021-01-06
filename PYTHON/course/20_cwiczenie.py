from collections import Counter

plik = open('words.txt', encoding='utf-8')


l = []

for e in plik:
    if len(e.strip()) > 3:
        l.append(e.strip())


zm = Counter(l)
zm = zm.most_common(10)

print(zm)





