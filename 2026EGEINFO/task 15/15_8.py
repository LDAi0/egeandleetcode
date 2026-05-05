def f(x,a):
    return ((x&52!=0)and(x&36==0))<=(not(x&a==0))

print(min([a for a in range(0,500) if all(f(x,a)==1 for x in range(0,1000))]))