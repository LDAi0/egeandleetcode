from functools import lru_cache
@lru_cache(100_100)
def is_iz(n):
    res=set()
    for i in range(2,int(n**0.5)):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    if len(res)==0: return True
    else: return False
print('temp')
n=0
for a in range(1,100_100):
    if n==20: break
    for b in range(0,100_100):
        if n==20: break
        if a*b>1_324_727 and ((str(a).count('5')==1)and(str(b).count('5')==1)):
            if is_iz(a) and is_iz(b):
                print(a*b,max(a,b))
                n+=1
            