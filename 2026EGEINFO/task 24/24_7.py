from re import *
from string import printable
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_9791_A.txt').readline()
#0123456789ABCDEF
p=r'[1223456789ABCDEF]+'
print(s[:100])
print(max([len(x.group()) for x in finditer(p,s)]))