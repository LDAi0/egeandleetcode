from functools import lru_cache
@lru_cache(None)
def f(n):
    if n<10: return n
    else: return f(n%10)+f(n//10)
cnt=0
for i in range(1,2**63):
    f(i)
    if f(i)==159:
        cnt+=1

