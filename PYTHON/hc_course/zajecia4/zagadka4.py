tab=[[],[]]
tab[0] = ["Time","Yellow","Painting","Energy"]
tab[1] = ["Pandemic","Yeti","Thor","Honey","Online","Numbers"]
a=""
for i in tab:
    for j in i:
        a+= j[0].lower()
    print(a)

