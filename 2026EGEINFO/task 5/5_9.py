from string import printable
def to_base(n,base):
    if n==0: return '0'
    res=''
    while n:
        res=printable[n%base]+res
        n//=base
    return res
print('temp')

for n in range(1,10000):
    r=to_base(n,2)
    if n%3==0:
        r=r+r[-3:]
    else:
        r=r+to_base((n%3)*3,2)
    r=int(r,2)
    if r>=200:
        print(n)
        break
