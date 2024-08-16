
from netmiko import ConnectHandler
CSR = {
    "device_type":"cisco_ios",
    "ip":"144.176.2.",
    "username":"admin",
    "password":"C1sco12345"
}

net_connect = ConnectHandler(**CSR)
route = net_connect.send_command('sh ip route')
run_confi = net_connect.send_command('sh run int Loopback 420')
run_vrf = net_connect.send_command('sh run vrf OMKAR')

print(route)
print(run_confi)
print(run_vrf)
net_connect.disconnect 

