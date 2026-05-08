from string import printable
def pere(n):
    if n==0: return 0
    res=''
    while n>0:
        res=printable[n%3]+res
        n//=3
    return res
for n in range(1,1000):
    r=pere(n)
    if n%3==0: 
        r=r+r[-2:]
    else:
        r=r+pere((n%3)*5)
    if int(r,3)>=290:
        print(n)
        break

