from functools import lru_cache

@lru_cache(100)
def f(n):
    if n<10: return n-1
    if n>=10 and n%2==0: return 3*n-1+f(n-3)
    if n>=10 and n%2!=0: return 5*n+2+f(n-4)

for i in range(4446):
    if i==4445: x=f(4445)
    if i==4444: x2=f(4444)
    f(i)

print(x-x2)