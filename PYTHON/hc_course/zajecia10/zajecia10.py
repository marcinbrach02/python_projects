# tworzenie zółwia i ruch po ekranie
# import turtle
# t = turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(150)
# t.right(50)
# t.backward(230)

# cw1
# import turtle
# t = turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(200)
# t.left(90)

# cw2
# import turtle
# t = turtle.Turtle()
# for i in range(2):
#     t.forward(100)
#     t.left(90)
#     t.forward(200)
#     t.left(90)

# cw3
# import turtle
# sides = [100, 200, 100, 200]
# t = turtle.Turtle()
# for side in sides:
#     t.forward(side)
#     t.left(90)

# cw4
# import turtle
# t = turtle.Turtle()
# t.forward(75)  # 150/2
# t.left(120)
# t.forward(150)
# t.left(120)     # 180 - 60
# t.forward(150)
# t.left(120)
# t.forward(75)

# cw5
# import turtle
# t = turtle.Turtle()
# n = int(input("Podaj liczbę kątów: "))
# inner_angle = (n-2)*180//n

# for x in range(n):
#     t.forward(100)
#     t.left(180-inner_angle)


# okrąg i kolory
# import turtle
# t = turtle.Turtle()
# t.fillcolor("GREEN")
# t.pencolor("RED")
# t.begin_fill()
# t.circle(50)
# t.end_fill()


# cw6
# import turtle
# t = turtle.Turtle()
##korona
# radius = 100
# t.color("GREEN")
# t.begin_fill()
# t.circle(radius)
# t.end_fill()
##pien
# heigh = 200
# width = 40
# t.color("BROWN")
# t.begin_fill()
# t.forward(width/2)
# t.right(90)
# t.forward(heigh)
# t.right(90)
# t.forward(width)
# t.right(90)
# t.forward(heigh)
# t.right(90)
# t.forward(width/2)
# t.end_fill()


# import turtle
# t = turtle.Turtle()
# t.pensize(8)
# t.shapesize(5)
##t.hideturtle()
# t.shape("turtle")
# t.forward(300)


# cw7
# import turtle
# import random
# shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

# for s in shapes:
#     t = turtle.Turtle()
#     t.shape(s)
#     t.left(random.randint(0, 360))
#     t.forward(150)

# cw8
# import turtle
# import random
# shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
# colors = ["red", "green", "blue", "black", "pink", "orange", "brown"]

# for s in range(10):
#     t = turtle.Turtle()
#     t.shape(random.choice(shapes))
#     t.color(random.choice(colors))
#     t.left(random.randint(0, 360))
#     t.forward(random.randint(100,200))


# Wyświetlanie kilku obiektów - żółwi
# import turtle
# stefan = turtle.Turtle()
# basia = turtle.Turtle()
# kasia = turtle.Turtle()

# stefan.forward(100)
# basia.shape("turtle")
# basia.backward(200)

# kasia.shape("square")
# kasia.left(90)
# kasia.forward(78)


# cw9
# import turtle
# x = 10
# t = turtle.Turtle()
# for i in range(10):
#     t.forward(x)
#     t.penup()
#     t.forward(x)
#     t.pendown()


# użycie klawiatury do ruchu żółwia
# import turtle
# t = turtle.Turtle()
# def go_forward():
#     t.forward(100)

# scr = turtle.Screen()
# scr.onkey(go_forward, "space")
# scr.listen()


# sterowanie klawiszami(gra 2D) - w,s,a,d
# import turtle
# t = turtle.Turtle()

# def up():
#     t.forward(100)
# def down():
#     t.backward(100)
# def left():
#     t.left(90)
# def right():
#     t.right(90)

# scr = turtle.Screen()
# scr.onkey(up, "w")
# scr.onkey(down, "s")
# scr.onkey(left, "a")
# scr.onkey(right, "d")
# scr.listen()


# użycie myszy do sterowania zółwiem
# import turtle
# def create_turtle(x, y):
#     t = turtle.Turtle(shape="turtle", visible=False)
#     t.speed(-1)
#     t.color("GREEN")
#     t.penup()
#     t.setpos(x, y)
#     t.shapesize(4)
#     t.showturtle()

# scr = turtle.Screen()
# scr.onscreenclick(create_turtle, 1)
# scr.listen()
