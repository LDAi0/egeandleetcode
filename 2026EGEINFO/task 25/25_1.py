from fnmatch import fnmatch
print('temp')
for x in range(2023,10**8+1,2023):
    if fnmatch(str(x),'3?1*57'):
        print(x,x//2023)