from fnmatch import fnmatch
def find_del(n):
    d=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    cnt=0
    sm=0
    for i in d:
        if i%2==0:
            cnt+=1
            sm+=i
    if cnt>=4: return sm
    else: return 0
cnt=0
for n in range(65_000,1_000_000):
    if cnt==7:
        break
    if fnmatch(str(n),'6*97*5?'):
        sm=find_del(n)
        if sm==0: 
            continue
        else: 
            print(n,sm)
            cnt+=1
    