from itertools import product

res=[]
cnt=0
for x in product('0123456',repeat=5):
    a=''.join(x)
    if a[0]=='0':continue
    if a.count('6')==1 and a[0]!=a[1] and a[1]!=a[2] and a[2]!=a[3] and a[3]!=a[4]:
        cnt+=1
print('temp',cnt)