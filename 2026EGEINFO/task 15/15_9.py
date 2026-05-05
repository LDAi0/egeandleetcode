def find_del(n):
    res=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return res
B=find_del(121)
for y in range(1,20000):
    C=find_del(y)
    if len(C)==0:
        continue
    if all(((x in C)<=((100<=x<=200)and(not(x in B))))==1 for x in range(-15000,15000)):
        print(y)
        break