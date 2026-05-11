from itertools import product
cnt=0
for x in product('агдепр',repeat=5):
    a=''.join(x)
    if a[0]!='а' and a[4]=='е' and a.count('г')==1:
        cnt+=1
print('temp',cnt)