m=[]
for x in range(1,2301):
    x1=7**350+7**150-x
    cnt=0
    while x1:
        if x1%7==0:
            cnt+=1
        x1//=7
    if cnt==200:
        m.append(x)
print(max(m))