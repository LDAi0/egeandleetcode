from turtle import *
screensize(5000,5000)
tracer(0)
m=70

left(90)

for _ in range(6):
    forward(33*m)
    right(90)
    forward(20*m)
    right(90)
penup()
forward(3*m)
right(90)
forward(9*m)
left(90)
pendown()
for _ in range(6):
    forward(24*m)
    right(90)
    forward(25*m)
    right(90)

penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()