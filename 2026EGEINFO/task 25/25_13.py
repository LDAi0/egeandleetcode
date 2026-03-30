from fnmatch import fnmatch
def find_d(n):
    res=set()
    mx=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
            if i!=n and i!=1:
                mx=max(mx,i)
                mx=max(mx,n//i)
            elif i==1:
                mx=max(mx,i)
            elif i==n:
                mx=max(mx,n//i)
    return [res,mx]
print('temp')
for i in range(10**9+1):
    if fnmatch(str(i),'15*3*09') and len(find_d(i)[0])==9:
        print(i,find_d(i)[1])