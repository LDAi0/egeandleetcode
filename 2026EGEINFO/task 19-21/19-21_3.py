print('temp')
def f(a,m):
    if a>=21: return m%2==0
    if m==0: return 0
    h=[f(a+1,m-1),f(a*2,m-1)]
    return any(h) if m%2!=0 else all(h)

print([s for s in range(1,21) if (not f(s,1)) and f(s,3)])
print([s for s in range(1,21) if (not f(s,2)) and (f(s,2) or f(s,4))])
print([s for s in range(1,21) if (not (f(s,1) or f(s,3))) and (not f(s,1)) and (f(s,1) or f(s,3) or f(s,5))])