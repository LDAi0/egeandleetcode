file=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 2\\17.txt')

def just(n):
    res=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return len(res)==2

a=[int(x) for x in file]
res=[]
for i in range(0,len(a)-2):
    if str(a[i]).count('3')>=1 and str(a[i+1]).count('3')>=1 and str(a[i+2]).count('3')>=1:
        if just(a[i]+a[i+1]+a[i+2]):
            res.append(a[i]+a[i+1]+a[i+2])
print('temp', len(res), min(res))
