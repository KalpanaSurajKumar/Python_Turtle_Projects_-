from turtle import *

t = Turtle()

s = getscreen()

t.speed(500)

s.bgcolor("black")

Color = ["red", "purple", "orange", "blue", "green", "pink"]

for i in range(360):
    t.color(Color[i % 5])
    t.width((i/100)+0.5)
    t.forward(i)
    t.left(150)
mainloop()