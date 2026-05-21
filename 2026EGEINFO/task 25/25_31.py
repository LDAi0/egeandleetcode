from fnmatch import fnmatch

def f(x):
    D=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            if fnmatch(str(i),'4*'):
                D.add(i)
            if fnmatch(str(x//i),'4*'):
                D.add(x//i)    
    return D

for x in range(0,10**6+1):
    D=sorted(f(x))
    if len(D)==24:
        print(x,D[-1])