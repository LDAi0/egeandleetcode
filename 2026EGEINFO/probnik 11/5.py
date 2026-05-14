def f(n):
    otv=""
    kek=False
    for i in n:
        if i=='1':
            if not kek:
                kek=True
                otv+='1'
            else:
                otv+='00'
        else:
            otv+='0'
    return otv


print('temp')
res=[]
for n in range(1,1000):
    r=bin(n)[2:]
    if n%2==0:
        r=r.replace('0','1')
    else:
        r=f(r)
    r=int(r,2)
    if r<=600:
        res.append([r,n])
print(sorted(res))