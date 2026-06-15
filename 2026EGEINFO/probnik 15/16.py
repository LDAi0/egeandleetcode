from functools import lru_cache

@lru_cache(200)
def f(n):
    if n>=129:
        return f(n-5)+1092
    else:
        return 5*g(n-7)+29
@lru_cache(300000)
def g(n):
    if n>303728: return n-15
    else: return g(n+8)/2-109

for i in range(310_000,0,-1):
    g(i)


for i in range(2100):
    f(i)
    if i==2049:
        x1=f(2049)
print(x1)