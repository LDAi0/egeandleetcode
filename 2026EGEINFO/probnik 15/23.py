def f(n,end):
    if n==end: return 1
    if n>end or n==16: return 0
    return f(n*2,end)+f(n**2,end)+f(n**3,end)
print(f(2,131072))
#14+23
