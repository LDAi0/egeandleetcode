from string import printable
def f(n):
    r=''
    while n>0:
        r=printable[n%7]+r
        n//=7
    return r
def sum_str(n):
    n=int(n)
    res1=0
    while n:
        res1+=n%10
        n//=10
    return res1
res=[]
for n in range(1,10_000):
    r=f(n)
    if sum_str(r)%2==0:
        r=r+'555'
    else:
        r='33'+r+'6'
    r=int(r,7)
    if r<12717:
        res.append(n)
print(max(res))