a=[int(x) for x in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 1\\9.txt')]
mx=max(x for x in a if x<0 and len(str(x))==5 and x%9==0)
res=[]
for i in range(0, len(a)-1):
    if (a[i]<0) + (a[i+1]<0) == 1:
        if (a[i]+a[i+1])>mx:
            res.append(a[i]**2+a[i+1]**2)
print('temp', len(res), min(res))

