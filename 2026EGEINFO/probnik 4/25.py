def find_del(n):
    res=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            res.append(i)
            res.append(n//i)
    return sorted(set(res))
print('temp')
for n in range(1_101_000,3_000_000):
    temp=[]
    for i in find_del(n):
        if len(find_del(i))==2:
            temp.append(i)
    m=max(temp)+min(temp)
    if m>13000 and m%100==26:
        print(n,m)