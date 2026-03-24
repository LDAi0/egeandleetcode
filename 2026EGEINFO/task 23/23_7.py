def f(n,end):
    if n>end or n==30: return 0
    if n==end: return 1
    return f(n+1,end)+f(n*2,end)+f(n*3,end)
print('remp', f(10,60)*f(60,70))