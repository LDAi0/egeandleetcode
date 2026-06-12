from math import dist 
f=open('C:\\Users\\abso\\Documents\\Visual Studio\\GoLeetcode\\2026EGEINFO\\task 27\\task_18184_B.txt')

# 1.5 1.7 3
# -25.2 -40.1 4
# 30.7 44.4 5

centr1bh=[1.5,1.7]
centr2bh=[-25.2,-40.1]
centr3bh=[30.7,44.4]
data=[]
for line in f:
    x,y=[float(k) for k in line.replace(',','.').split()]
    data.append([x,y])
print(len(data))

bh1=[p for p in data if 3<=dist(centr1bh,p)<=9]
bh2=[p for p in data if 4<=dist(centr2bh,p)<=12]
bh3=[p for p in data if 5<=dist(centr3bh,p)<=15]
print(len(bh1),len(bh2),len(bh3))

sr1=int((sum([dist(centr1bh,p)-3 for p in bh1])/len(bh1))*1000)
sr2=int((sum([dist(centr2bh,p)-4 for p in bh2])/len(bh2))*1000)
sr3=int((sum([dist(centr3bh,p)-5 for p in bh3])/len(bh3))*1000)
print(sr1,sr2,sr3)
# 2439 3408

# 3408 2439
# 6561 3294