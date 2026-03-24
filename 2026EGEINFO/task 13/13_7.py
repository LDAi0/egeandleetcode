from ipaddress import ip_network
net=ip_network('156.132.15.138/255.255.252.0',0)
i=0
for ip in net:
    print('govnop', i,ip)
    i+=1