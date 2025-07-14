from turtle import *

s=getscreen()

t=Turtle()
t.width(5)
t.speed(100)

for i in range(1000):
    t.left(i*90)
    t.forward(i*5)

mainloop()