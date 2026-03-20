from fnmatch import fnmatch
print('temp')

for x in range(237,10**8+1,237):
    if fnmatch(str(x),'81?2*80') and not fnmatch(str(x), '*9*') :
        print(x,x//237)