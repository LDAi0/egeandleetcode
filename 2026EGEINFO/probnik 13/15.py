def f(x):
    P=25<=x<=240
    Q=175<=x<=300
    R=270<=x<=340
    A=a1<=x<=a2
    return (Q<=P) or ((not A)<=R)

r=[y for x in {25,175,240,270,300,340} for y in {x,x-0.1,x+0.1}]
res=[]
for a1 in r:
    for a2 in r:
        if a2>=a1 and all(f(x)==1 for x in r):
            res.append(a2-a1)
print(min(res))