f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 12/1.txt')
cnt=0

for line in f:
    a=[int(x) for x in line.split()]
    pov=[x for x in a if a.count(x)==3]
    nepov=[x for x in a if a.count(x)==1]
    if len(pov)==3 and len(nepov)==4:
        if (sum(pov)/len(pov))>=(sum(nepov)/len(nepov)):
            cnt+=1
print(cnt)