from functools import lru_cache

@lru_cache(100)
def f(n):
    if n<=2:
        return 2*1024
    if n>=3:
        return 2*n+3+f(n-2)

for i in range(4049):
    if i==4048:
        x1=f(4048)
    if i==16:
        x2=f(16)
    f(i)

print(x1-x2)