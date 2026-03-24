from string import printable
def sum_d(n):
    return sum(int(x) for x in n)

def f(n,base):
    if n==0: return '0'
    res=""
    while n>0:
        res=printable[n%base]+res
        n//=base
    return res

print('govno')
ans=[]

for n in range(0,10000):
    r=f(n,3)
    if sum_d(r)%3==0:
        r=r+'212'
    else:
        r=r+f(sum_d(r)*2,3)
    if int(r,3)>490:
        ans.append(int(r,3))
print(min(ans))
        

