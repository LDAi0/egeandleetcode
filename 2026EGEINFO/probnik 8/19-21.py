def f(a,b,m):
    if a+b>=342: return m%2==0
    if m==0: return 0
    h=[f(a+2,b,m-1),f(a*5,b,m-1),f(a,b+2,m-1),f(a,b*5,m-1)]
    return any(h) if m%2!=0 else all(h)
print([s for s in range(1,326) if f(11,s,2)])
print([s for s in range(1,326) if (not f(11,s,1)) and f(11,s,3)])
print([s for s in range(1,326) if (not f(11,s,2)) and (f(11,s,2) or f(11,s,4)) ])