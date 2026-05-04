from fnmatch import fnmatch
for x in range(84318,10**11,84318):
    if fnmatch(str(x),'5*7?') and len(str(x))==len(set(str(x))):
        print(x,x//84318)