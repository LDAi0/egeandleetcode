from functools import lru_cache
@lru_cache(1000)

def f(n):
    if n<=5:
        return 1
    else:
        return n+f(n-2)

for i in range(2126): f(i)

print('te,mp', f(2126)-f(2122))

