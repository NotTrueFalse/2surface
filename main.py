import turtle
import time
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
def aire(cote:float)->float:
    return cote**2

def sqrt(x:float)->float:
    return x**0.5

def rnd_hex()->str:
    return "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])

def abs(x:float)->float:
    if x < 0:
        return -x
    return x

def ceil(x:float)->float:
    """Renvoie la partie entière supérieure de x"""
    if x == int(x):
        return x
    return int(x)+1

def carre(x, y, couleur,size):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(couleur)
    # turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    screen.update()
    return aire(size)
cote = 1
mult = 2
aire_ = carre(0, 0, "red", cote)
s = 0
for x in range(int(40/mult)):
    s += 1
    turtle.left(90/(4-mult))
    cote = sqrt(mult*aire_)
    aire_ = ceil(carre(0, 0, rnd_hex(), cote))
    print(aire_,"cm²","step",s)
    time.sleep(1/240)
screen.mainloop()
