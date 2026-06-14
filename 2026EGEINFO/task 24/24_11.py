from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_17756_A.txt').readline()

p=r'(([+*][0123456789]+)+)[+*]?'
g=r'(([0123456789]+[+*])+)[+*]?'
print(s[:100])
print(max([len(x.group()) for x in finditer(p,s)]))
print(max([len(x.group()) for x in finditer(g,s)]))

