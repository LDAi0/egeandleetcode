f=open("C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 5\\1.txt")
cnt=0
for line in f:
    n=0
    a=[int(x) for x in line.split()]
    pov=[int(x) for x in a if a.count(x)==3]
    nepov=[int(x) for x in a if a.count(x)==1]
    for i in range(0,len(a)-1):
        if a[i]<=a[i+1]:
            n+=1
        else: break
    if ((n==6) + (len(pov)==3 and len(nepov)==4))<=1:
        cnt+=1
print('temp',cnt)
