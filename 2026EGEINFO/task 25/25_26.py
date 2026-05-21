from fnmatch import fnmatch

def f(n):
    D=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0: 
            D.add(i)
            D.add(n//i)
    return D

for koren_x in range(1,int((int(10**9)+1)**0.5)):
    x=koren_x**2
    if fnmatch(str(x),'15*3*09'):
        D=sorted(f(x))
        if len(D)==9:
            print(x,D[-2])
