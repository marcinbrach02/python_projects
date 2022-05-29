# ad1
#a
# import turtle
# coder = turtle.Turtle()
# for i in range(5):
#     coder.forward(100)
#     coder.left(72)

#b
# import turtle
# coder = turtle.Turtle()
# for i in range(4):
#     coder.forward(50)
#     coder.left(90)
#     coder.forward(50)
#     coder.right(90)

# ad2
#a - sześcioramienna gwiazda
# import turtle
# coder = turtle.Turtle()
# for i in range(6):
#     coder.right(60)
#     coder.forward(50)
#     coder.left(120)
#     coder.forward(50)

#b - spirala
# import turtle
# coder = turtle.Turtle()
# x=1
# while True:
#     coder.forward(x)
#     coder.left(15)
#     x = x + 1
#     if x == 60:
#         break

# przy uzyciu petli for
# m = 1
# for i in range(100):
#   coder.forward(m+i)
#   coder.right(m*15)

#c - prostokąt z wygumowanymi rogami
# import turtle
# t = turtle.Turtle()
# sides = [100, 200, 100, 200]
# x = 10 #wielkość wymazanego obszaru
# for side in sides:
#     t.penup()
#     t.forward(x)
#     t.pendown()
#     t.forward(side)
#     t.penup()
#     t.forward(x)
#     t.left(90)


# ad3
import turtle, random
t = turtle.Turtle()
scr = turtle.Screen()
t.shape("turtle")
t.left(90)

def left_up():
    t.left(45)
    t.forward(100)
def up():
    t.forward(100)
def right_up():
    t.right(45)
    t.forward(100)

def left():
    t.left(90)
    t.forward(100)
def right():
    t.right(90)
    t.forward(100)

def change_color():
    colors = ["red", "green", "blue", "black", "pink", "orange", "brown"]
    t.color(random.choice(colors))

def raise_or_drop():
    if t.isdown():
        t.penup()
    else:
        t.pendown()


def left_down():
    t.right(45)
    t.backward(100)
def down():
    t.backward(100)
def right_down():
    t.left(45)
    t.backward(100)

def bigger():
    w,h,o = t.shapesize()
    t.shapesize(1.2*w, 1.2*h)

def lower():
    t.shapesize(i-1)


scr.onscreenclick(bigger, 3)
scr.onscreenclick(lower, 1)

scr.onkey(left_up, "7")
scr.onkey(up, "8")
scr.onkey(right_up, "9")

scr.onkey(left, "4")
scr.onkey(change_color, "5")
scr.onkey(right, "6")

scr.onkey(left_down, "1")
scr.onkey(down, "2")
scr.onkey(right_down, "3")
scr.onkey(raise_or_drop, "0")

scr.listen()
turtle.mainloop()

# dkoknczyc
