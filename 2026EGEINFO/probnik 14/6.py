from turtle import *
screensize(2000,2000)
tracer(0)
m=20

left(90)

for _ in range(3): fd(2*m); rt(90); fd(3*m); lt(90)
rt(180); fd(6*m); rt(90); fd(9*m)
penup()
backward(3*m); rt(90)
pendown()
for _ in range(2): fd(1*m); rt(90); fd(2*m); lt(90)
rt(180); fd(3*m); rt(90); fd(4*m); rt(90); fd(1*m)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()