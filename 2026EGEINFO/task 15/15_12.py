def f(x):
    P=66<=x<=67
    O=32<=x<=125
    T=30<=x<=491
    A=a1<=x<=a2
    return (not A)<=(P or (not O) or (not T))

r=[y for x in {30,32,66,67,125,491} for y in {x,x-0.1,x+0.1}]
res=[]
for a1 in r:
    for a2 in r:
        if a2>=a1 and all(f(x)==1 for x in r):
            res.append(a2-a1)
print(round(min(res)))
