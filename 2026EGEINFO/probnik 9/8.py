from itertools import product
n=1
for x in product('алпця',repeat=5):
    a=''.join(x)
    if a.count('а')<=1 and a.count('ц')==2 and a.count('л')==0:
        print(n)
        break
    n+=1