res=[]
for n in range(0,10000):
    r = bin(n)[2:]
    if r.count('0')%2==0:
        r='1'+r+'1'
    elif r.count('0')%2!=0:
        r='10'+r
    if int(r,2)<100:
        res.append(int(r,2))
print('temp', max(res))