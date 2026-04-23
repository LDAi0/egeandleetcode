def f(n,base):
    digits="0123456789"
    if n==0: return '0'
    res=""
    while n>0:
        res=digits[n%base]+res
        n//=base
    return res
cnt=0
res=[]
print('temp')
for n in range(1,100000):
    r=f(n,8)
    if n%7==0:
        r+=str(int(f(n,8))%100)
    else:
        r+=f((n%7)*7,8)
    if int(r,8)<3000:
        res.append(int(r,8))
print('temp',len(set(res)))