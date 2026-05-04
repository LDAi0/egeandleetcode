def find_m(n):
    res=set()
    for d in range(2,int(n**0.5)):
        if n%d==0:
            res.add(d)
            res.add(n//d)
    if len(res)==0:
        return 0
    return min(res)+max(res)
print('temp')
x=0
for n in range(800_001,810_000):
    if x==5:
        break
    if find_m(n)%10==4:
        print(n,find_m(n))
        x+=1