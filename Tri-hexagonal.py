from turtle import *

bgcolor('black')

speed(0)

pencolor('navy blue')


def des():
    for i in range(3):
        for j in range(5):
            fd(60)
            right(60)
        fd(60)
        lt(60)
        fd(60)


for i in range(36):
    des()
    right(10)

mainloop()
