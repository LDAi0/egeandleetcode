s=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 17\\1.txt')
res=[]
a=[int(x) for x in s]
mx=max([x for x in a if len(str(x))==5 and x<0 and x%9==0])
for i in range(len(a)-1):
    if ((a[i]<0) + (a[i+1]<0))==1:
        if (a[i]+a[i+1])>mx:
            res.append(a[i]**2+a[i+1]**2)
print('temp', len(res), min(res))
