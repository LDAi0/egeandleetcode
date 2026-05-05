f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 8\\1.txt')

a=[int(x) for x in f]
res=[]
for i in range(0,len(a)-3):
    if ((abs(a[i])%100==13)+(abs(a[i+3])%100==13))==1:
        res.append(a[i]+a[i+3])
print('temp',len(res),max(res))