from re import *

f=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_9845_A.txt').readline()

p=r'(([ABC][89])+)|(([89][ABC])+)'
print(f[:100])
print(max([len(x.group()) for x in finditer(p,f)]))