from turtle import *
screensize(6000,6000)
tracer(0)
m=30

left(90)

for _ in range(9):
    forward(50*m)
    right(90)
    forward(35*m)
    right(90)
penup()
forward(5*m)
right(90)
forward(10*m)
right(90)
pendown()
for _ in range(4):
    forward(35*m)
    right(90)
    forward(17*m)
    right(90)

penup()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()