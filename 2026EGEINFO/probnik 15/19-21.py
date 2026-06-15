def f(a,m):
    if a==0:return m%2==0
    if m==0: return 0
    if a>=5:
        h=[f(a-5,m-1),f(a//3,m-1)]
    else:
        h=[f(a//3,m-1)]
    return any(h) if m%2!=0 else all(h)
print([s for s in range(1,10_000) if (not f(s,1)) and f(s,2)])
print([s for s in range(1,10_000) if (not f(s,1)) and f(s,3)])
print([s for s in range(1,10_000) if (not f(s,2)) and (f(s,2) or f(s,4))])

