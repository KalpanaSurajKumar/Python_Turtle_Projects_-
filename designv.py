from turtle import *

s = getscreen()

t = Turtle()

for i in range(1000):
    t.dot(i)
    t.penup()
    t.rt(i+90)
    t.forward(600)
    pendown()

mainloop()

