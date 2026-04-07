from functools import lru_cache
@lru_cache(None)
def f(n):
    if n<222: return 111
    else: return 2*(n+4)+f(n-3)

print('temp')

for i in range(55555): f(i)

print(f(55555)-f(55543))