cnt=0
index=0
max_index=-1
for line in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 9\\9_1.txt'):
    a=[int(x) for x in line.split()]
    p3=[int(x) for x in a if a.count(x)==3]
    p2=[int(x) for x in a if a.count(x)==2]
    np=[int(x) for x in a if a.count(x)==1]
    if len(p3)==3 and len(p2)==2 and len(np)==3:
        if (sum(p3)+sum(p2))>sum(np):
            if index>max_index:
                cnt=sum(a)
    index+=1
print('temp',cnt)