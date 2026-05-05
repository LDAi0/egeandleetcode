from string import printable
def per(n):
    res=''
    if n==0:
        return 0
    while n>0:
        res=printable[n%3]+res
        n//=3
    return res
def sum_num(n):
    x=int(n)
    res=0
    while x>0:
        res+=x%10
        x//=10
    return res
for n in range(1,1000):
    r=per(n)
    if n%3==0:
        r=r+r[-2:]
    else: 
        r=r+per(sum_num(r))
    if int(r,3)%2==0 and int(r,3)>220:
        print('temp',int(r,3))
        break