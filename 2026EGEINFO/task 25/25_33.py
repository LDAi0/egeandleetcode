def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d)==0:
        return 0
    return min(d)+max(d)
i=0
for x in range(700_000,810_000):
    m=f(x)
    if i==6: break
    if m%10==4:
        print(x,m)
        i+=1
