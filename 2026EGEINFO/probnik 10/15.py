def f(x,y,a):
    return (78125!=(y+(4*x))) or ((a>x) and (a>y))

#print('tem,p',min([a for a in range(0,2500) if all(f(x,y,a)==1 for x in range(1,100) for y in range(1,100))]))
for a in range(1,10000):
    if all(f(x,y,a)==1 for x in range(1,10000) for y in range(1,10000)):
        print('temp',a)