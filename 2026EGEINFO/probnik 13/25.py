from fnmatch import fnmatch

def f(x):
    D=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            D.add(i)
            D.add(x//i)
    return D

for koren_x in range(1,int((10**7+1)**0.5)):
    x=koren_x**2
    D=sorted(f(x))
    if fnmatch(str(x),'3*52?') and len(D)%2!=0:
        print(x,D[-2])