cnt=0
for line in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 9\\9_1.txt'):
    a=[int(x) for x in line.split()]
    nepov=[x for x in a if a.count(x)==1]
    pov=[x for x in a if a.count(x)==3]

    if len(pov)==3 and len(nepov)==3:
        if sum(nepov)**2<sum(pov)**2:
            cnt+=1

print('dasd',cnt)