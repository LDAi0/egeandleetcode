from itertools import product

cnt=0

for x in product('агийнф',repeat=4):
    a=''.join(x)
    for c in 'аи': a=a.replace(c,'а')
    if a[0]!='й':
        if a.count('а')>=1:
            cnt+=1
print(cnt)