import turtle
t = turtle.Turtle()
t.hideturtle()
turtle.bgcolor('black')

# Making window
t.penup()
t.setposition(-100, 110)
t.pendown()
t.begin_fill()
t.fillcolor("#00adef")
t.pencolor("#00adef")
t.left(10)
t.forward(200)
t.right(100)
t.forward(220)
t.right(100)
t.forward(200)
t.right(80)
t.forward(153)
t.end_fill()

# Making line to cut the window

t.penup()
t.setposition(-100, 34)
t.pendown()
t.right(90)
t.width(10)
t.color('black')
t.fd(200)

t.penup()
t.setposition(0, 200)
t.right(90)
t.pendown()
t.fd(300)

# Writing windows

t.goto(80, -150)
t.color('white')
t.write('Windows', font=('Arial', 26, 'normal'))
t.penup()
t.goto(300, -300)
t.pendown()

t.write('Made by\n Suraj kumar Jha\n from Madhubani,Bihar', font=('Arial', 20, 'normal'))

turtle.mainloop()
