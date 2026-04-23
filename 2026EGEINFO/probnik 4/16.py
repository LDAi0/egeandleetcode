from functools import lru_cache

@lru_cache(None)
def f(n):
    if n<11: return n
    return n+f(n-1)

for i in range(1,2024): f(i)

print('temp', f(2024)-f(2021))