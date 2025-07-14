import turtle
s=turtle.getscreen()

turtle.hideturtle()
t1 = turtle.Turtle()

t1.fillcolor("light blue")
t1.begin_fill()
for i in range(4):
    t1.forward(300)
    t1.lt(90)
t1.end_fill()

t1.penup()

t1.goto(0,70)
t1.forward(30)

t1.pendown()
t1.fillcolor("red")

t1.begin_fill()
for i in range(4):
    t1.forward(50)
    t1.rt(90)
t1.end_fill()
t1.penup()

t1.goto(300,0)

t1.penup()
t1.goto(300,70)

t1.backward(30)
t1.rt(90)
t1.fillcolor("green")
t1.pendown()
t1.begin_fill()
for i in range(4):
    t1.forward(50)
    t1.rt(90)
t1.end_fill()

t1.penup()
t1.goto(300,300)

t1.forward(70)
t1.rt(90)

t1.forward(30)
t1.fillcolor("yellow")
t1.pendown()

t1.begin_fill()
for i in range(4):
    t1.forward(50)
    t1.rt(90)
t1.end_fill()

t1.penup()

t1.goto(0,300)

t1.lt(90)
t1.forward(70)
t1.lt(90)
t1.forward(30)

t1.pendown()
t1.fillcolor("purple")
t1.begin_fill()
for i in range(4):
    t1.forward(50)
    t1.lt(90)
t1.end_fill()
t1.ht()

turtle.mainloop()


