def f(a,m):
    if a>=281: return m%2==0
    if m==0: return 0
    h=[f(a+4,m-1),f(a*2,m-1)]
    return any(h) if m%2!=0 else all(h)
print('temp')
print([s for s in range(1,281) if (not f(s,1)) and f(s,2)])
print([s for s in range(1,281) if (not f(s,1)) and f(s,3)])
print([s for s in range(1,281) if (f(s,2) or f(s,4)) and (not f(s,2))])
