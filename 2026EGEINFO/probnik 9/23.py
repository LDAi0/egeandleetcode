def f(n,end,m):
    if n>end or m>3: return 0
    if n==end: return 1
    return f(n+2,end,m)+f(n*3,end,m+1)+f(n*5,end,m+1)
print(f(2,200,0))