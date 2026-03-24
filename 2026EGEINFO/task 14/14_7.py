def f(n):
    cnt=0
    while n>0:
        if n%11==0:
            cnt+=1
        n//=11
    return cnt

ans=[]
for x in range(1,3001):
    x1=9*11**210+8*11**150-x
    if f(x1)==60:
        ans.append(x)
print('govno', max(ans))
