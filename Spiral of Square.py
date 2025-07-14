from turtle import *

speed(0)

bgcolor('black')
pencolor('red')

for i in range(10, 240):
    for j in range(4):
        fd(i)
        right(90)
    right(10)
    if i>=120 and i<=200:
        pencolor("green")


mainloop()
