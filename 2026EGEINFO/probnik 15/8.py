from itertools import product
m=[]
n=1
for x in product('ЕКМОПРТЬЮ', repeat=5):
    a=''.join(x)
    if n%2==1 and a[0]!='Ь' and a.count('К')==2:
        m.append(n) 
    n+=1
print(max(m))