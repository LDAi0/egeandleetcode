def f(x):
    P=12<=x<=28
    Q=15<=x<=30
    A=a1<=x<=a2
    return (P<=A) and ((not Q) or A)
print('temp')
r=[y for x in {12,15,28,30} for y in {x,x-0.1,x+0.1}]
res=[]
for a1 in r:
    for a2 in r:
        if all(f(x)==1 for x in r) and a2>=a1:
            res.append(a2-a1)
print(round(min(res)))
