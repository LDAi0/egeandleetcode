def f(n,end):
    if n>end or n==13: return 0
    if n==end: return 1
    return f(n+1,end)+f(n+2,end)+f(n*3,end)
print('temp', f(3,8)*f(8,18))