def f(n,end):
    if n<end or n==36: return 0
    if n==end: return 1
    return f(n-3,end)+f(n-6,end)+f(n//2,end)

print('govno',f(86,53)*f(53,12))