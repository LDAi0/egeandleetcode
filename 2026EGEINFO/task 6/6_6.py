from turtle import *
screensize(2000,2000)
tracer(0)
m=100

left(90)

for _ in range(4):
    forward(4*m)
    left(270)
    forward(5*m)
    right(90)
left(270)
for _ in range(3):
    forward(3*m)
    right(90)
    forward(3*m)
    left(270)
penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(7,'red')
done()