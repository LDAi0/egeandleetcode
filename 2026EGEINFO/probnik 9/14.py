from string import printable
res=[]
cnt_max=0
for x in range(1,2031):
    h=7**170+7**100-x
    cnt=0
    while h>0:
        if h%7==0:
            cnt+=1
        h//=7
    if cnt>=cnt_max:
        res.append(x)
print(max(res))
