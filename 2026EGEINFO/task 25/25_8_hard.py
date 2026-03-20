from fnmatch import fnmatch
print('temp')
cnt=1
for x in range(4546,10**10+1,4546):
    if fnmatch(str(x),'8*80*06') :
        if cnt%60==1:
            print(x,x//4546)
        cnt+=1