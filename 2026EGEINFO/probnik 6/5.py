res=[]
for n in range(1,100000):
    r=bin(n)[2:]
    if n%5==0:
        r=r[:3]+r
    else:
        r=r+bin(n%5)[2:]
    if int(r,2)<313 and n%2!=0:
        res.append(n)
print('temp', max(res))