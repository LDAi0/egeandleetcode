def f(x):
    P=35<=x<=55
    Q=45<=x<=65
    A=a1<=x<=a2
    return P<=A
def g(x):
    P=35<=x<=55
    Q=45<=x<=65
    A=a1<=x<=a2
    return (not A)<=(not Q)

h=[y for x in (35,45,55,65) for y in (x,x-0.1,x+0.1)]
r=[]
print('temp')
for a1 in h:
    for a2 in h:
        if all((f(x) and g(x))==1 for x in h) and a2>=a1:
            r+=[a2-a1]
print(round(min(r)))