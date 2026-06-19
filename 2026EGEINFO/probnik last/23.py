def f(n,end):
    if n>end or n==43: return 0
    if n==end: return 1
    return f(n+2,end)+f(n+(n-1),end)+f(n+(n+1),end)
print(f(7,63))