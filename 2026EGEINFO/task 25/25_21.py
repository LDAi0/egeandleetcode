import re
res=[]
for x in range(4546,10**10+1,4546):
    if re.fullmatch(r'8\d*80\d*06',str(x)):
        res.append([x,x//4546])
for i in range(0,len(res)):
    if i%60==0:
        print(*res[i])