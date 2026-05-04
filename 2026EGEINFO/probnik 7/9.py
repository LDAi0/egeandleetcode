f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 7\\1.txt')

n=1

for line in f:
    a=[int(x) for x in line.split()]
    pov=[x for x in a if a.count(x)==2]
    nepov=[x for x in a if a.count(x)==1]
    if len(pov)==4 and len(nepov)==3 and len(set(pov))==2:
        if (sum(pov)/len(pov))<max(nepov):
            print('',n)
            break
    n+=1