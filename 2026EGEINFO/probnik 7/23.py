def f(n,end):
    if n>end: return 0
    if n==end: return 1
    return f(n+4,end)+f(n*2,end)

print('', f(13,42))