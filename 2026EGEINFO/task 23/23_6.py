def f(n,end):
    if n>end: return 0
    if n==end: return 1
    return f(n+1,end)+f(n+3,end)+f(n*3,end)
print('remp', f(3,9)*f(9,27)*f(27,31))