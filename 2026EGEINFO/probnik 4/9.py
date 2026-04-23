f=open("C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 4\\1.txt")
cnt=0
print('temp')
for line in f:
    a=[int(x) for x in line.split()]
    pov=[x for x in a if a.count(x)==3]
    nepov=[x for x in a if a.count(x)==1]
    if len(pov)==3 and len(nepov)==4:
        if (sum(nepov)/len(nepov))<=pov[0]:
            print(sum(nepov)/len(nepov),pov[0])
            cnt+=1
print('temp',cnt)