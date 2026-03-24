from fnmatch import fnmatch

cnt=0
print('govno')

for x in range(7993,10**10+1,7993):
    if fnmatch(str(x),'4*4736*1'):
        print(x,x//7993)