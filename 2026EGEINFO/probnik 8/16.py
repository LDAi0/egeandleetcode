from functools import lru_cache
@lru_cache(None)
def f(n):   
    if n<1000: return 66
    else: return f(n-5)+100
for i in range(180_001): f(i)

print('temp',f(180_000)-f(100_000))