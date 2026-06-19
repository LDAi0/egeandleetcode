from functools import lru_cache
@lru_cache(100)
def f(n): 
    if n<5: return  n
    else:  
        return 2*n*f(n-4)

for i in range(14000):
    if i==13766:
        x1=f(13766)
    if i==13762:
        x2=f(13762)
    if i==13758:
        x3=f(13758)
    f(i)

print((x1-9*x2)/x3)