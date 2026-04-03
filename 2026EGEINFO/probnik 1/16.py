from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
#@lru_cache(None)
def f(n):
    if n>7000: return n+4
    else: return 3*n+5+f(n+3)
#for i in range(0,100): f(i)
#for i in range(1000,2000): f(i)    
print('temp', f(707)-f(716))