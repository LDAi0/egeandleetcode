from turtle import *
screensize(10000,10000)
tracer(0)
m=80

left(90)

right(30)
for _ in range(3):
    right(150)
    forward(6*m)
    right(30)
    forward(12*m)
penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(7,'red')
done()