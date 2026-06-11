def f(a,m,p,v,who):
    if a>=29: return m%2==0
    if m==0: return 0
    if who:
        if p==0:
            h=[f(a+1,m-1,1,v,not who),f(a+2,m-1,2,v,not who),f(a*2,m-1,3,v,not who)]
        elif p==1:
            h=[f(a+2,m-1,2,v,not who),f(a*2,m-1,3,v,not who)]
        elif p==2:
            h=[f(a+1,m-1,1,v,not who),f(a*2,m-1,3,v,not who)]
        elif p==3:
            h=[f(a+1,m-1,1,v,not who),f(a+2,m-1,2,v,not who)]
    if not who:
        if v==0:
            h=[f(a+1,m-1,p,1,who),f(a+2,m-1,p,2,who),f(a*2,m-1,p,3,who)]
        elif p==1:
            h=[f(a+2,m-1,p,2,who),f(a*2,m-1,p,3,who)]
        elif p==2:
            h=[f(a+1,m-1,p,1,who),f(a*2,m-1,p,3,who)]
        elif p==3:
            h=[f(a+1,m-1,p,1,who),f(a+2,m-1,p,2,who)]
    return any(h) if m%2!=0 else all(h)

print([s for s in range(1,29) if (not f(s,1,0,0,True)) and f(s,3,0,0,True)])
print([s for s in range(1,29) if (not f(s,2,0,0,True)) and f(s,4,0,0,True)])
print([s for s in range(1,29) if not (f(s,1,0,0,True) or f(s,3,0,0,True)) and f(s,5,0,0,True)])