print('temp')
res=[]
for n in range(1,100000):
    r=bin(n)[2:]
    if r.count('1')%2==0:
        r=r+'11'
    elif r.count('1')%2!=0:
        r=r+'01'
    else: continue
    if int(r,2)>61: 
        res.append(int(r,2))
print(min(res))
