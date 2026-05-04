from turtle import *
screensize(5000,5000)
tracer(0)
m=50

left(90)

for _ in range(2):
    forward(24*m)
    right(90)
    forward(10*m)
    right(90)
forward(3*m)
left(90)
forward(13*m)
right(90)
for _ in range(2):
    forward(9*m)
    right(90)
    forward(32*m)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()