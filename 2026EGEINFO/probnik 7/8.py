from itertools import product
n=1
res=[]
cnt=0
for x in product('абеилртфц', repeat=5):
    a=''.join(x)
    if n%2!=0 and a[0] not in 'аеи' and a.count('ф')==a.count('ц'):
        cnt+=1
    n+=1
print('', cnt)