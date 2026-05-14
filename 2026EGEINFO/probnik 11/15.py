def f(x):
    P=257<=x<=1000
    Q=5<=x<=100
    R=99<=x<=258
    A=a1<=x<=a2
    return (A<=R) and ((not(A<=P))<=Q)
r=[y for x in [5,99,100,257,258,1000] for y in [x,x-0.1,x+0.1]]
res=[]
for a1 in r:
    for a2 in r:
        if a2>=a1 and all(f(x)==1 for x in range(1,2000)):
            res.append(a2-a1)
print('temp',round(min(res)))