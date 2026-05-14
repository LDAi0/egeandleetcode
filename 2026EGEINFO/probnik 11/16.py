from functools import lru_cache

@lru_cache(100)
def f(n):
    if n<5: return 4**4
    if n>4: return 4*f(n-4)+4

for i in range(0,4050):
    if i==4048:
        x1=f(i)
    if i==4036:
        x2=f(i)
    f(i)

print(f(4048)/f(4036))