from fnmatch import fnmatch
print('temp')
for x in range(8387,10**9+1,8387):
    if fnmatch(str(x),'*75?122*'):
        print(x,x//8387)