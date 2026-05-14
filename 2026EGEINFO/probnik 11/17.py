f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 11\\2.txt')
a=[int(x) for x in f]
mn=min([x for x in a if 100<=abs(x)<=999 and abs(x)%10==3])
res=[]
for i in range(0,len(a)-1):
    if (1000<=a[i]<=9999)+(1000<=a[i+1]<=9999)==1:
        if ((a[i]**2)+(a[i+1]**2))%mn==0:
            res.append((a[i]**2)+(a[i+1]**2))
print('temp',len(res),max(res\))