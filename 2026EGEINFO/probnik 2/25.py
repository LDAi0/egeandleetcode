def f(n):
    res=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    if len(res)==2: return True
    else: return False
print('temp')
for x in range(1324727,10_000_000):
    for i in range(0,x+1):
        if f(i) and str(i).count('5')==1:
            for l in range(i,x+1):
                if f(i) and str(i).count('5')==1:
                    if i*l==x:
                        print(x,max(l,i))
       