from functools import lru_cache

@lru_cache(1000)
def f(n):
    if n<3:
        return n+1
    if n>=3 and n%2==0:
        return f(n-2)+n-2
    return f(n+2)+n+2

cnt=0
for i in range(0,10000):
    f(i)
    if 10000<=f(i)<=99999:
        cnt+=1