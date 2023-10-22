# ad1
tab = [5, 15, 1, 25, 2]
print(tab[0])
print(tab[2])
print(tab[-1])
print(tab[-3])
#print(tab[10])
print(len(tab))
print(max(tab))
print(sum(tab))
print(sorted(tab))
print(sorted(tab, reverse = True))

# ad2
x = 1234
print(type(x))
x = [1, 2, 3, 4]
print(type(x))
x = {1, 2, 3, 4}
print(type(x))
x = {1:2, 3:4}
print(type(x))
x = (1, 2, 3, 4)
print(type(x))
x = 1, 2, 3, 4
print(type(x))

# ad3
my_dict = { "january" : 3459.32,
            "february" : 3478.30,
            "march" : 3502.50
            }

minimum = min(my_dict.values())
print("Wartość minimalna: " + str(minimum))
maximum = max(my_dict.values())
print("Wartość maksymalna: " + str(maximum))
amount = sum(my_dict.values())
print("Suma: " + str(amount))
average = sum(my_dict.values()) / len(my_dict)
print("Średnia: " + str(average))

lenght = len(my_dict)
months = list(my_dict.keys())
last_month = months[lenght-1]
last_month_value = my_dict[str(last_month)]

if last_month_value >= average:
    print("Zacznij oszczędzać!")
else:
    print("Jesteś bezpieczny")

# ad4
numbers = input("Podaj 5 różnych cyfr oddzielonych przecinkiem: ")
numbers = list(numbers.split(","))
print(numbers)
lenght = len(numbers)

if lenght != 5:
    print("Nie podałeś 5 cyfr!")
else:
    numbers = set(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    x = numbers.pop()
    print("Wylosona cyfra to: " + str(x))

    if x == maximum:
        print("Wylosowano maksymalna cyfre!")
    elif x == minimum:
        print("Wylosowano najmniejszą cyfrę!")
