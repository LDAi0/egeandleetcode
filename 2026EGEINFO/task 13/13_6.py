from ipaddress import ip_network
net=ip_network('172.16.80.0/255.255.248.0',0)
cnt=0
for ip in net:
    if int(bin(int(ip))[2:].count('1'))%2!=0:
        cnt+=1
print('temp', cnt)