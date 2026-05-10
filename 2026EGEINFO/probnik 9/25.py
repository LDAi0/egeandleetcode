def find_m(n):
    res=set()
    for i in range(2,int(n**0.5)):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    if len(res)==0: return 0
    return min(res)+max(res)
n=0
for i in range(800_000,1_500_000):
    if find_m(i)%10==4:
        print(i,find_m(i))
        n+=1
    if n==5: break