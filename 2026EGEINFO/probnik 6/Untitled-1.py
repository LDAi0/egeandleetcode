f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 6\\1.txt')
a=[int(x) for x in f]
mn=min([x for x in a if x>=100 and x<=999 and abs(x)%10==7])
res=[]
for i in range(0,len(a)-1):
    if ((a[i]>=100 and a[i]<=999) + (a[i+1]>=100 and a[i+1]<=999))==1:
        if (a[i]+a[i+1])%mn==0:
            res.append(a[i]+a[i+1])
print('temp', len(res), min(res))