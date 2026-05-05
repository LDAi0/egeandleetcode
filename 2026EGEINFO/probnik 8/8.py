from string import printable
from itertools import product
cnt=0
#abcdef
for x in product(printable[:16],repeat=3):
    a=''.join(x)
    if a[0]!='0':
        if a[0]!=a[1] and a[1]!=a[2] and a[0]!=a[2]:
            for c in '02468ace': a=a.replace(c,'0')
            for c in '13579bdf': a=a.replace(c,'1')
            if '11' not in a and '00' not in a:
                cnt+=1
print('temp',cnt)