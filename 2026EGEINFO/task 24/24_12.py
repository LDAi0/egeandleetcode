from re import *
s=open('/home/abso/Code/egeandleetcode/2026EGEINFO/task 24/task_12931_A.txt').readline()
p=r'((VWXYZ)|(WXYZ)|(XYZ)|(YZ)|Z)?(VWXYZ)+((VWXYZ)|(VWXY)|(VWX)|(VW)|V)?'
print(s[:1000])
print(max([len(x.group()) for x in finditer(p,s)]))


