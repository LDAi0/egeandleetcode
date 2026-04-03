from fnmatch import fnmatch
print('tmep')
for x in range(253,10**8+1,253):
    if fnmatch(str(x),'12??15*6'):
        print(x,x//253)
