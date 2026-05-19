from ipaddress import ip_network
net=ip_network('95.24.20.25/255.255.252.0',0)
cnt=0
for ip in net.hosts():
    cnt+=1
print(cnt-1-3-4-2-1)