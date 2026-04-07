cnt=0
for line in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\probnik 2\\9.txt'):
    a=[int(x) for x in line.split()]
    pov=[x for x in a if a.count(x)==2]
    nepov=[x for x in a if a.count(x)==1]
    chet=[x for x in a if x%2==0]
    nechet=[x for x in a if x%2!=0]
    if len(chet)==0:
        arifchet=0
    else: arifchet=sum(chet)/len(chet)
    if len(nechet)==0:
        arifnechet=0
    else: arifnechet=sum(nechet)/len(nechet)
    if (len(set(pov))==1 and len(set(nepov))==4) + (abs(arifchet-arifnechet)>50)==1:
        cnt+=1
       
print('temp',cnt)