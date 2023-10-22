# ad1
# tab = [1, 50,10]
# for k in tab:
#     print(k)

# for i in range(5):
#     print(i-1)
#     print(i+3)

# a = 3
# while a < 10:
#     print(a / 2)
#     a = a + 2


# ad2
# for i in range(0,13,3):
#     print(i)

# i=3
# while i > -4:
#     print(i)
#     i = i-1


# ad3
# tabx = [1,3,5,7]
# taby = [2,4,6]
# for x in tabx:
#     for y in taby:
#         if (x != 3 and y != 2):
#             print(x, y)


# ad4
# rozwiązanie w skrypcie


# ad5
# products = input("Podaj produkty oddzielonych przecinkiem: ")
# products = set(products.split(","))
# products = set(products)

# products_items = {}

# for product in products:
#     price = input("Podaj cene dla produktu " + product + ": ")
#     products_items.update({product : price} )

# for key, value in products_items.items():
#     print("Cana dla " + key + " to: " + value)


# ad6
# counter = 0
# while True:
#     print("Wartość licznika: " + str(counter))
#     counter = counter + 1
#     if counter == 1:
#         break


# ad7
# my_dict = { "january" : 61.32,
#             "february" : 21.30,
#             "march" : 31.50,
#             "april" : 41.21,
#             "may" : 51.21,
#             "june" : 61.41
#             }

# average = sum(my_dict.values()) / len(my_dict)
# print("Średnia: " + str(average))

# for key in my_dict.keys():
#     if my_dict[key] > average:
#         print("Wartości dla " + key + " to: " + str(my_dict[key]))


# ad8
# numbers = input("Podaj 5 różnych cyfr oddzielonych przecinkiem: ")
# numbers = list(numbers.split(","))

numbers = [1258,75544,2333,5435.67,43656790]

print(numbers)

lenght = len(numbers)

for number in numbers:
    number = int(number)
    numbers[lenght-1] = number
    lenght = lenght - 1
    print(number)

print(numbers)
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








