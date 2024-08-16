
#It imports the ConnectHandler class from the netmiko module and defines a dictionary CSR with the device configuration details. 
#This dictionary is used to establish a connection to a Cisco IOS device.
from netmiko import ConnectHandler
CSR = {
    "device_type":"cisco_ios",
    "ip":"x.x.x.x",
    "username":"admin",
    "password":"C1sco12345"
}
#establishes a connection to a Cisco IOS device using the ConnectHandler class and the CSR dictionary. 
#It then sends commands to retrieve the routing table, configuration of a specific interface (Loopback 420), and configuration of a specific VRF (OMKAR).
net_connect = ConnectHandler(**CSR)
route = net_connect.send_command('sh ip route')
run_confi = net_connect.send_command('sh run int Loopback 420')
run_vrf = net_connect.send_command('sh run vrf OMKAR')



print(route)
print(run_confi)
print(run_vrf)
net_connect.disconnect 



