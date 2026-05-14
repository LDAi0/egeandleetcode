from functools import lru_cache

@lru_cache(100)
def f(n):
    if n>2000: return 16
    if n<=2000:return 2*f(n+3)

for i in range(112):
    if i==50: x1=f(50)
    if i==110: x2=f(110)
    f(i)
print(x1//x2)
