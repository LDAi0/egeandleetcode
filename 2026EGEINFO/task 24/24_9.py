from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_6636_A.txt').readline()

p=r'([24][135])+'
print(max([len(x.group()) for x in finditer(p,s)]))
