from turtle import *
screensize(2000,2000)
tracer(0)
m=20

left(90)

for _ in range(4):
    fd(19*m); rt(90); fd(30*m); rt(90)
up()
fd(2*m); rt(90); fd(8*m); lt(90)
down()
for _ in range(4):
    fd(93*m); rt(90); fd(97*m); rt(90)
up()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()