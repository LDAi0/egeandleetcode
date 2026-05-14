from itertools import product

n=1

for x in product('иклнор',repeat=4):
    a=''.join(x)
    if a=='кино':
        print('temp',n)
    n+=1