import re

def f(x):
    D=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            D.add(i)
            D.add(x//i)
    return D

for x in range(53,10**7+1,53):
    if re.fullmatch(r'\d*2\d2\d*',str(x)):
        if str(x)==str(x)[::-1]:
            D=f(x)
            if len(D)>30:
                print(x,sum(D))
