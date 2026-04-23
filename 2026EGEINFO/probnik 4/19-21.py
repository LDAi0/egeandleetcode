def f(a,m,q):
    if a>40: return m%2==0
    if m==0: return 0
    if q==0: h=[f(a+3,m-1,1),f(a+6,m-1,2),f(a*2,m-1,3)]
    elif q==1: h=[f(a+6,m-1,2),f(a*2,m-1,3)]
    elif q==2: h=[f(a+3,m-1,1),f(a*2,m-1,3)]
    elif q==3: h=[f(a+3,m-1,1),f(a+6,m-1,2)]
    return any(h) if m%2!=0 else all(h)

print([s for s in range(2,37) if (not f(s,1,0)) and f(s,2,0)])
print([s for s in range(2,37) if (not f(s,1,0)) and f(s,3,0)])
print([s for s in range(2,37) if (not f(s,2,0)) and (f(s,2,0) or f(s,4,0)) ])