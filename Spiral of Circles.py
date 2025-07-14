from turtle import *

bgcolor("black")
pensize(2)
speed(0)
hideturtle()
ls = ['red', 'yellow', 'white', 'blue', 'cyan', 'green']

for i in range(60):
    for colo in ls:
        color(colo)
        circle(60)
        left(10)

mainloop()
