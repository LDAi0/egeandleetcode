from turtle import *
screensize(5000,5000)
tracer(0)
m=50

left(90)

for _ in range(13):
    forward(10*m)
    right(90)
    forward(10*m)
    right(90)
    forward(30*m)
    right(90)

penup()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()