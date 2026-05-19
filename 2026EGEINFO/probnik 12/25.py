from fnmatch import fnmatch

def f(n):
    res=0
    while n>0:
        res+=n%10
        n//=10
    if res%7==0 and res<20:
        return True
    else: return False

for x in range(2023,10**9+1,2023):
    if fnmatch(str(x),'20*23') and f(x):
        print(x)