from turtle import *
screensize(5000,5000)
tracer(0)
m=50

left(90)

for _ in range(4):
    forward(16*m)
    left(90)
    forward(20*m)
    left(90)
penup()
forward(4*m)
left(90)
forward(8*m)
right(180)
pendown()
for _ in range(3):
    forward(35*m)
    left(90)
    forward(6*m)
    left(90)
penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()
