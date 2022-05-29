import turtle

a=turtle.Turtle()
a.up()
a.backward(50)
a.right(90)
a.forward(100)
a.left(90)
a.down()
a.fillcolor("BLUE")
a.begin_fill()


for x in range(5):
    a.forward(200)
    a.left(180-108)
a.end_fill()
a.hideturtle()

b=turtle.Turtle()
b.color("WHITE")
b.begin_fill()
for i in [100,50,100,50]:
    b.forward(i)
    b.right(90)
b.end_fill()
b.hideturtle()

c = turtle.Turtle()
c.up()
c.forward(45)
c.down()
c.color("RED")
c.begin_fill()
for i in [10,50,10,50]:
    c.forward(i)
    c.right(90)
c.end_fill()
c.hideturtle()

d = turtle.Turtle()
d.up()
d.right(90)
d.forward(20)
d.down()
d.color("RED")
d.begin_fill()
for i in [10,100,10,100]:
    d.forward(i)
    d.left(90)
d.end_fill()
d.hideturtle()
