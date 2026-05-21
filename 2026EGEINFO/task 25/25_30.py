from fnmatch import fnmatch

def f(x):
    D=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            D.add(i)
            D.add(x//i)
    return D

for koren_x in range(1,int((int(10**7)+1)**0.5)):
    x=koren_x**2
    if fnmatch(str(x),'3*52?'):
        D=sorted(f(x))
        if len(D)%2==1:
            print(x,D[-2])
    
