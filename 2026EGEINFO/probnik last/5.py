from string import printable
def summa(n):
    res=0
    while n:
        res+=n%10
        n//=10
    return res


def to_base(n):
    if n==0:
        return '0'
    res=''
    while n:
        res=printable[n%3]+res
        n//=3
    return res


m=[]
for n in range(1,100000):
    r=to_base(n)
    if summa(int(r))%2==0:
        r='1'+r+'2'
    else:
        r='2'+r+'0'
    r=int(r,3)
    if r>100:
        m.append(r)
print(min(m))

