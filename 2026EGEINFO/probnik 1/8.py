from itertools import product
from string import printable
cnt=0
print('temp', printable[:13])
for x in product(printable[:13],repeat=7):
    a=''.join(x)
    if a[0]=='0': continue
    is_need=True
    for i in '0123456789abc':
        if a.count(i)<=1: continue
        else: is_need=False
    for i in '13579': a = a.replace(i,'1')
    if '1b' not in a and 'b1' not in a and is_need: cnt+=1
print(cnt)


