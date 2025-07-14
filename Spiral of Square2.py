import turtle
from random import randint

s = turtle.getscreen()
a = turtle.Turtle()
s.bgcolor('black')

col = ['white', 'orange', 'red', 'yellow', 'green', 'blue', 'cyan']

a.speed(500)

for i in range(200):
    a.fd(i * 4)
    a.right(91)
    a.color(col[randint(0, 6)])
    for b in range(3):
        a.forward(i * 4)
        a.right(91)
        for c in range(2):
            a.forward(i * 4)
            a.right(91)

turtle.mainloop()
