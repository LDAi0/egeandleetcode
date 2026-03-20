def f(n,end):
    if n>end or n==11 or n==12: return 0
    if n==end: return 1
    return f(n+1,end)+f(n*2,end)+f(n**2,end)
print('temp', f(2,10)*f(10,40))