from turtle import *
screensize(2000,2000)
tracer(0)
m=50

left(90)

for _ in range(3):
    forward(2*m)
    right(90)
    forward(3*m)
    left(90)
right(180)
forward(6*m)
right(90)
forward(9*m)
penup()
backward(3*m)
right(90)
pendown()
for _ in range(2):
    forward(1*m)
    right(90)
    forward(2*m)
    left(90)
right(180)
forward(3*m)
right(90)
forward(4*m)
right(90)
forward(1*m)
penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()