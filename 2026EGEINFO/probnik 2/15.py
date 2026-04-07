def f(x):
    b=36<=x<=75
    c=60<=x<=110
    A=a1<=x<=a2
    return (not A)<=((b)==(c))
r=[]
print('temp')
d=[y for x in (36,60,75,110) for y in (x,x-0.1,x+0.1)]
for a1 in d:
    for a2 in d:
        if all(f(x)==1 for x in d) and a2>=a1:
            r+=[a2-a1]
print(round(min(r)))