from turtle import *
screensize(5000,5000)
tracer(0)
m=50

left(90)

for _ in range(5):
    forward(15*m)
    left(90)
    forward(25*m)
    left(90)
penup()
forward(4*m)
left(90)
forward(12*m)
left(90)
pendown()
for _ in range(6):
    forward(38*m)
    right(90)
    forward(22*m)
    right(90)
penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()