from turtle import *

bgcolor('black')
speed(0)

col = ['white', 'orange', 'red', 'yellow', 'green', 'blue', 'cyan']

for i in range(120):
    pencolor(col[i % 6])
    circle(190 - i / 2, 90)
    left(90)
    circle(190 - i / 3, 90)

    left(60)

mainloop()
