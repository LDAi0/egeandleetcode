f=open("C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 4\\1.txt")
a=[int(x) for x in f]
mx=max(a)
res=[]
for i in range(0,len(a)-2):
    c=[a[i],a[i+1],a[i+2]]
    otr=[x for x in c if x<0]
    pol=[x for x in c if x>0]
    if abs(sum(otr))<=sum(pol):
        if int(str(a[i]*a[i+1]*a[i+2])[-1])==(mx%10):
            res.append(abs(a[i]*a[i+1]*a[i+2]))
print('tem,p', len(res),max(res))