import turtle

s = turtle.getscreen()
turtle.ht()
t1 = turtle.Turtle()
t1.pensize(2)
t1.speed(1)
t1.pencolor("blue")
t1.penup()
t1.goto(-200,-50)
t1.pendown()
t1.fillcolor("pink")
t1.begin_fill()
t1.lt(60)
t1.fd(400)
t1.rt(120)
t1.fd(400)
t1.rt(120)
t1.fd(400)
t1.penup()
t1.goto(200,180)
t1.pendown()
t1.forward(400)
t1.lt(120)
t1.fd(400)
t1.lt(120)
t1.fd(400)
t1.end_fill()
t1.ht()


turtle.mainloop()
