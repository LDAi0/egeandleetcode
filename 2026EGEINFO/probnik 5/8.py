from itertools import product
n=1
for x in product('агмнсту',repeat=6):
    a=''.join(x)
    if a[0]!='у' and a.count('м')==2 and a.count('г')<=1:
        print(n)
    n+=1
