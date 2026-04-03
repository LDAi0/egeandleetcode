def f(n,end):
    if n>end or n==14: return 0
    if n==end: return 1
    return f(n+1,end)+f(n+3,end)
print('temp', f(2,9)*f(9,18))
