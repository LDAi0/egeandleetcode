f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/probnik 14/9.txt')
cnt=0    
for line in f:
    a=[int(x) for x in line.split()]
    if (max(a)+min(a))<=(sum(a)-(max(a)+min(a))):
        cnt+=1
print(cnt)