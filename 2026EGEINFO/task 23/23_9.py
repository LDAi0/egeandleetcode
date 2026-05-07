def f(n,end):
    if n>end or n==16: return 0
    if n==end: return 1
    return f(n+1,end)+f(n+3,end)+f(n*2,end)
print(f(3,9)*f(9,30))