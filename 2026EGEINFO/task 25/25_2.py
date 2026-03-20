from fnmatch import fnmatch
print('temp')
for x in range(151,10**9+1,151):
    if fnmatch(str(x), '2?34?56?8'):
        print(x,x//151)