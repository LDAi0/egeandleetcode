from string import printable
def f(n,base):
    res=''
    while n>0:
        res=printable[n%base]+res
        n//=base
    return res
print('temp')
res=[]
for n in range(1,100000):
    r=f(n,3)
    if n%5==0:
        r=r+r[-3:]
    else:
        r=r+f((n%5)*5,3)
    r=int(r,3)
    if r<5496:
        res.append(n)
print(max(res))