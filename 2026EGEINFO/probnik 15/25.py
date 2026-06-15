def deli(n):
    d=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    if len(d)==0:
        return 0
    else:
        return min(d)+max(d)
i=0
print('dawd')
for n in range(800_001,900_000):
    
    if i==6: break
    M=deli(n)
    if M%10==4:
        print(n,M)
        i+=1
    