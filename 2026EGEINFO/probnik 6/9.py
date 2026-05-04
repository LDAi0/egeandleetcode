n=1
print('temp')
res=[]
for line in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 6\\1.txt'):
    a=[int(x) for x in line.split()]
    pov3=[x for x in a if a.count(x)==3]
    nepov=[x for x in a if a.count(x)==1]
    if len(pov3)==3 and len(nepov)==4:
        if (sum(pov3)/len(pov3))>(sum(a)/len(a)):
            print(n)
    n+=1