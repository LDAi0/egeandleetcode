from turtle import *
screensize(10000,10000)
tracer(0)
m=20

left(90)

for _ in range(4): fd(2*m); rt(90) 
up()
fd(10*m); left(180)
down()
for _ in range(4): fd(23*m); rt(90); fd(3*m); rt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*m,y*m)
        dot(5,'red')
done()