from fnmatch import fnmatch
print('temp')

def sum_d(n):
    return sum(int(x) for x in str(n))

for x in range(2023,10**9+1,2023):
    if fnmatch(str(x), '20*23'):
        if sum_d(x)%7==0 and sum_d(x)<20:
            print(x)