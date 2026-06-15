from turtle import *
m=20
tracer(0)
screensize(5000,5000)

left(90)

for _ in range(5):
    fd(15*m); lt(90); fd(25*m); lt(90)
up()
fd(4*m); lt(90); fd(12*m); lt(90)
down()
for _ in range(6): 
    fd(38*m); rt(90); fd(22*m); rt(90)

up()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()