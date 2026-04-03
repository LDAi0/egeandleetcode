def f(n,m):
    if n>=88: return m%2==0
    if m==0: return 0
    h=[f(n+1,m-1),f(n+4,m-1),f(n*3,m-1)]
    return any(h) if m%2!=0 else all(h)
print('temp')
print([s for s in range(1,88) if (not f(s,1)) and f(s,2)])
print([s for s in range(1,88) if (not f(s,1)) and f(s,3)])
print([s for s in range(1,88) if (not f(s,2) and (f(s,2) or f(s,4)))])