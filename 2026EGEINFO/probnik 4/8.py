from itertools import permutations
cnt=0
for x in set(permutations('анастасия')):
    a=''.join(x)
    for n in 'аия': a=a.replace(n,'a')
    for n in 'нст': a=a.replace(n,'n')
    if ('nnn' in a) and ('aaa' in a):
        continue
    cnt+=1
print('temp',cnt)
    
