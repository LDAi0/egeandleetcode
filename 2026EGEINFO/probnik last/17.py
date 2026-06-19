f=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\probnik last\task_23757_A.txt')
a=[int(x) for x in f]
mn=min([x for x in a if 10<=abs(x)<=99])
res=[]
for i in range(0,len(a)-1):
    if ((10<=abs(a[i])<=99)+(10<=abs(a[i+1])<=99))==1:
        if (a[i]+a[i+1])%mn==0:
            res.append(a[i]+a[i+1])
print(len(res), max(res))