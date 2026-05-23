def f(n,end):
    if n==end: return 1
    if n>end or n==12: return 0
    return f(n+1,end)+f(n+2,end)+f(n*3,end)
print(f(2,9)*f(9,19))