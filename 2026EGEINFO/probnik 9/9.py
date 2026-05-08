f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 9/1.txt')
n=0
for line in f:
    a=[int(x) for x in line.split()]
    if (100<=a[0]<=999)+(100<=a[1]<=999)+(100<=a[2]<=999)+(100<=a[3]<=999)+(100<=a[4]<=999)+(100<=a[5]<=999)>=3:
        if a[0]%5!=0 and a[1]%5!=0 and a[2]%5!=0 and a[3]%5!=0 and a[4]%5!=0 and a[5]%5!=0:
            n+=1
print(n)