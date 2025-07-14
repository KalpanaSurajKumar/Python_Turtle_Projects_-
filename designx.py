from turtle import *
import random

s = getscreen()

t = Turtle()

s.bgcolor("black")

t.width(4)
t.speed(1)
t.rt(90)


c = ["red", "green", "blue",  "yellow", "pink", "orange", "cyan"]

j=300
for x in range(10):
    t.color(c[random.randint(0,6)])
    t.circle(j)
    j=j-30

mainloop()
