from fnmatch import fnmatch

def f(x):
    D=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            if i%2==0:
                D.add(i)
            if x//i%2==0:
                D.add(x//i)
    return D

for x in range(65001,100_100_100):
    if fnmatch(str(x),'6*97*5?'):
        D=f(x)
        if len(D)>=4:
            print(x,sum(D))
