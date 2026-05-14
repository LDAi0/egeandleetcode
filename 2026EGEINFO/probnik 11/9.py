s=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 11\\1.txt')
def f(n):
    if len(n)==0:
        return 0
    return sum(n)/len(n)

cnt=0
for line in s:
    a=[int(x) for x in line.split()]
    pov=[x for x in a if a.count(x)==2]
    nepov=[x for x in a if a.count(x)==1]
    chet=[x for x in a if x%2==0]
    nchet=[x for x in a if x%2!=0]
    if (len(pov)==2 and len(nepov)==4)+(abs(f(chet)-f(nchet))>50)==1:
        cnt+=1
print('temp',cnt)