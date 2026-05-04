def f(n,end):
    if n>end: return 0
    if n==end: return 1
    return f(n+1,end)+f(n+2,end)+f(n*2,end)


print('temp', f(3,25))