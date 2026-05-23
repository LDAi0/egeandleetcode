f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 13/task_21990_A.txt')
a=[int(x) for x in f]
res=[]
for i in range(0,len(a)-2):
    c=a[i:i+3]
    otr=[x for x in c if x<0]
    pol=[x for x in c if x>0]
    if abs(sum(otr))<=sum(pol):
        if (abs(c[0]*c[1]*c[2])%10)==(max(a)%10):
            res.append(abs(c[0]*c[1]*c[2]))
print(len(res), max(res))