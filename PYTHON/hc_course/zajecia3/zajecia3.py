# listy
tab = [5, 15, 1, 25, 2] #deklaracja listy
print(tab)
print(tab[0])
print(tab[1])
print(tab[-1])
# print(tab[10]) - błąd index po za zakresem

print(len(tab))
print(max(tab))
print(min(tab))
print(sum(tab))
print(sum(tab)/len(tab)) # średnia arytmetyczna
print(sorted(tab))

# cw1
names = ["Marcin", "Szymon", "Dorota", "Ola"]
print(sorted(names)) # sortowanie wg ascii najpierw duże litery(wartości sa mniejsze)

# operacje na listach:
my_list = [11, 12, 13]
my_list[1] = 15 # wstawienie pod index 1
print(my_list)
my_list.append(18) # dodawanie na koniec listy
print(my_list)
my_list.insert(2,14) #dodajemy pod index 2 wartosc 14
print(my_list)

x = my_list.pop() # pobranie ostatniego elementu z listy i wstawienie go do x
print(my_list)
print(x)
my_list.reverse() # odwrócenie kolejności elementów w tablicy
print(my_list)

my_list1 = [1, 2, 3]
my_list2 = [4, 5]
large_list = my_list1 + my_list2 # dodanie dwóch list
print(large_list)
new_list = large_list * 3 # pomnożenie listy
print(new_list)

print(new_list[0:4]) # wyswietlenie 4 pierwszych elementów
print(new_list[:4])
print(new_list[8:15]) # wyswietlenie zakresu wartości z listy 8-15
print(new_list[8:])
print(new_list[1:15:2]) # wyświetlenie od 1 do 8 co drugi element
print(new_list[4:0:-1])
print(new_list[::-1]) # odrócenie tj. reverse

#krotki
my_tuple = (22, 55, 66) # tworzenie krotki - niewymagane nawiasy(niezalecane)
print(my_tuple)
print(my_tuple[1])
print(len(my_tuple))
x = (1, 2) + (3, 4) # suma krotek (tupli)
print(x)

#słowniki
my_dict = { "apples" : 5,
            "bananas" : 10 ,
            "oranges" : 15 }

print(my_dict)
print(my_dict["apples"])
print(my_dict["oranges"])
print(my_dict.keys()) # wyświetenie kluczy
print(my_dict.values()) # wyświetlenie wartości
print(my_dict.items()) # wyświetlenie słownika

points = { (0,0) : 5,
           (1,2) : 10
            }
print(points[(0,0)]) # odwołanie się do pierwszego klucza w słowniku

my_dict = {1: "jeden", 2: "dwa"}
my_dict.update({3:"trzy"}) # update słownika o nowy klucz
print(my_dict)
my_dict[4] = "cztery" # jesli klucz nie istnieje to sie stworzy
print(my_dict)
del my_dict[2] # usunięcie klucza 2
print(my_dict)

# cw2
basket = {"chleb" : 3.50 , "masło" : 2.0 , "ser" : 4}
print(basket)
print(sum(basket.values()))

#set (zbór)
my_set = {1,2,4} # tworzenie zbioru (setu)
print(my_set)
my_set.add(5) # dodawanie elementu do zbioru
print(my_set)
my_set.add(99)
print(my_set)
my_set.add(99)
print(my_set)

my_set.remove(4) # usuniecie 4 elementu ze zbioru
print(my_set)

x = my_set.pop() # pobraniepierwszego elementu ze zbioru
print(x)
print(my_set)
print(5 in my_set) # czy 5 jest w secie jesli True to tak

# napisy
name = "HardCoder" # tworzenie napisu
print(name[1]) # odwoływanie się do drugiej litery
print(name[4:8])
print(name[::-1])
