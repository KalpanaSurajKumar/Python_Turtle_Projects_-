import turtle

# To create the screen
s = turtle.getscreen()
# to hide the default  turtle
turtle.ht()

# To create the Turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# Tp pick the pencolor of the turtle
t1.pencolor("blue")
t2.pencolor("red")
x = t1
y = t2
# To choose the thickness of the turtle
t1.pensize(2)
t2.pensize(2)
t1.penup()
t2.penup()
t1.goto(-400, 0)
t2.goto(400, 0)
t2.lt(180)
t1.pd()
t2.pd()
for i in range(1, 11):
    t2.forward(70)
    t2.penup()
    t2.fd(10)
    t2.pendown()
for i in range(100):

    for i in range(1, 11):

        for j in range(4):
            t2.undo()
        t1.forward(70)
        t1.penup()
        t1.fd(10)
        t1.pendown()


    for i in range(1, 11):
        for j in range(4):
            t1.undo()
        t2.forward(70)
        t2.penup()
        t2.fd(10)
        t2.pendown()

turtle.mainloop()
