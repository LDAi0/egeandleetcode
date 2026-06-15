f=open(r'C:\Users\abso\Documents\Visual Studio\GoLeetcode\2026EGEINFO\probnik 15\9.txt')

for line in f:
    a=[int(x) for x in line.split()]
    pov=[x for x in a if a.count(x)==2]
    nepov=[x for x in a if a.count(x)==1]
    if len(set(pov))==2 and len(nepov)==3:
        if max(a) not in pov:
            print('etm',sum(a))
            break
