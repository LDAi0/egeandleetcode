from turtle import *
screensize(5000,5000)
tracer(0)
m=50

left(90)

for _ in range(10):
    forward(22*m)
    right(90)
    forward(16*m)
    right(90)
penup()
forward(1*m)
right(90)
forward(1*m)
left(90)
pendown()
for _ in range(10):
    forward(72*m)
    right(90)
    forward(79*m)
    right(90)
penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()