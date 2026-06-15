f=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\probnik 15\task_23276_A.txt')
a=[int(x) for x in f]
mx=max([x for x in a if abs(x)%100==25])
res=[]
for i in range(0,len(a)-2):
    if ((1000<=abs(a[i])<=9999)+(1000<=abs(a[i+1])<=9999)+(1000<=abs(a[i+2])<=9999))<=2:
        if (a[i]+a[i+1]+a[i+2])<=mx:
            res.append(a[i]+a[i+1]+a[i+2])
print('etmp', len(res), max(res))