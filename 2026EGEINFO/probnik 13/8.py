from itertools import product

n=1
for x in product('агилморт',repeat=5):
    a=''.join(x)
    if n%2==0 and a[0]!='а' and a[0]!='г':
        if a.count('р')>=2:
            print(n)
            break
    n+=1