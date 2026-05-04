from itertools import product,permutations
res=[]
print('temp')
n=1
for x in product('аекнот', repeat=7):
    a=''.join(x)
    if n%2!=0:
        for i in set(permutations('еккноот')):
            s=''.join(i)
            if a==s:
                print(n)
    n+=1