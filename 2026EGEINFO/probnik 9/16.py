from functools import lru_cache

def f(n):
    return g(n-1)
@lru_cache(100)
def g(n):
    if n<=9: return 3*n
    else:
        return g(n-1)+1

for i in range(47995): g(i)

print(f(47995))
