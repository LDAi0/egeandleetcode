from itertools import product

n=1
m=[]
for x in product('БГДНОУШ', repeat=6):
    a=''.join(x)
    if n%2==1:
        if a[0]!='Б':
            if a.count('Н')>=2 and a.count('У')==0:
                m.append(n)
    n+=1
print(max(m))