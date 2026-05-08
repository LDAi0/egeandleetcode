from turtle import *
screensize(5000,5000)
tracer(0)
m=50

left(90)

for _ in range(5):
    forward(37*m)
    right(90)
    forward(44*m)
    right(90)
penup()
backward(18*m)
right(90)
forward(29*m)
left(90)
penup()
for _ in range(5):
    forward(31*m)
    right(90)
    forward(35*m)
    right(90)

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()