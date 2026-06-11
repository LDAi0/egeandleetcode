def find_R(n):
    d=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return d
i=0
for x in range(500_000, 600_000):
    if i==6:
        break
    d=find_R(x)
    if sum(d)%10==6:
        print(x,sum(d))
        i+=1