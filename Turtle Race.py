from turtle import *
from random import randint

z = Turtle()
z.fd(1)
# Making the turtles
t1 = Turtle()

t1.shape('turtle')
t1.color('red')
t1.width(5)
t1.penup()
t1.setposition((-120, -150))
t1.pendown()
t1.left(90)

# creating second turtle
t2 = Turtle()
t2.shape('turtle')
t2.color('green')
t2.width(5)
t2.penup()
t2.setposition(-50, -150)
t2.pendown()
t2.left(90)

# creating 3rd turtle
t3 = Turtle()
t3.shape('turtle')
t3.color('yellow')
t3.width(5)
t3.penup()
t3.setposition(20, -150)
t3.pendown()
t3.left(90)

# Creating 4th turtle
t4 = Turtle()
t4.shape('turtle')
t4.color('blue')
t4.width(5)
t4.penup()
t4.setposition(90, -150)
t4.pendown()
t4.left(90)

# Creating 5th turtle
t5 = Turtle()
t5.shape('turtle')
t5.color('cyan')
t5.width(5)

t5.penup()
t5.setposition(160, -150)
t5.pendown()
t5.left(90)

z.penup()
z.setposition(160, 200)
z.pendown()
z.pensize(2)
z.backward(400)
z.lt(90)
z.fd(40)
z.rt(90)
z.fd(400)
z.rt(90)
z.fd(40)

z.bk(20)
z.rt(90)
z.fd(400)
z.penup()
z.lt(90)
z.bk(20)
z.pendown()
c = ["red", "green", "blue", "yellow"]

for i in range(10):
    z.color(c[randint(0, 3)])
    z.left(90)
    z.fd(40)
    z.rt(90)
    z.fd(40)
    z.bk(40)
    z.hideturtle()

for i in range(100):
    t1.fd(randint(1, 6))

    t2.fd(randint(1, 6))
    t3.fd(randint(1, 6))
    t4.fd(randint(1, 6))
    t5.fd(randint(1, 6))

pos = [t1.position(), t2.position(), t3.position(), t4.position(), t5.position()]
ps2 = []
print(pos)
for cord in pos:
    ps2.append(cord[1])

m = [t1, t2, t3, t4, t5]

for x in m:
    if x.position()[1] == max(ps2):
        for s in range(12):
            x.lt(90)



mainloop()
