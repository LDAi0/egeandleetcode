from re import  *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_4602_A.txt').readline()

p=r'([BCD][AO])+'
print(s[:200])
print(max([len(x.group()) for x in finditer(p,s)]))