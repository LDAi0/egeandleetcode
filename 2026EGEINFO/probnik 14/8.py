from string import printable
from itertools import product
#0123456789a
print(printable[:12])
cnt=0
for x in product(printable[:12], repeat=7):
    a=''.join(x)
    if a[0]!='0':
        if a.count('b')==2:
            for c in '02468a': a=a.replace(c,'2')
            for c in '13579b': a=a.replace(c,'1')
            if '22' not in a and '11' not in a:
                cnt+=1
print(cnt)
            