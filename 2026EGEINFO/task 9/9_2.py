cnt=0
for line in open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 9\\9_1.txt'):
    a=[int(x) for x in line.split()]
    chet=[x for x in a if x%2==0]
    nechet=[x for x in a if x%2!=0]
    if len(a) == len(set(a)):
        if len(chet)>len(nechet):
            cnt+=1
print('asdasd', cnt)