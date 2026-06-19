def f(x):
    B=36<=x<=75
    C=60<=x<=110
    A=a1<=x<=a2
    return (not A)<=(B==C)

r=[y for x in {36,60,75,110} for y in {x,x-0.1,x+0.1}]
res=[]
for a1 in r:
    for a2 in r:
        if a2>=a1 and all(f(x) for x in r):
            res.append(a2-a1)
print(round(min(res)))
