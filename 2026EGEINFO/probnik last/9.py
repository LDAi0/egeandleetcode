f=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\probnik last\9.txt')
cnt=0
for line in f:
    a=[int(x) for x in line.split()]
    pov=[x for x in a if a.count(x)==2]
    nepov=[x for x in a if a.count(x)==1]
    if len(set(pov))==3 and len(nepov)==1:
        if ((min(pov)+max(pov))/2)<max(nepov):
            cnt+=1
print(cnt)