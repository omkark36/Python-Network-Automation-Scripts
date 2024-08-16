
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


#The commands are executed using the send_command method of the net_connect object. 
#The results are stored in the route, run_confi, and run_vrf variables, respectively.

route = net_connect.send_command('sh ip route')
run_confi = net_connect.send_command('sh run int Loopback 420')
run_vrf = net_connect.send_command('sh run vrf OMKAR')



print(route)
print(run_confi)
print(run_vrf)

#net_connect.disconnect, is used to close the network connection established with the Cisco IOS device. 
#This is an essential step to free up system resources and ensure that the connection is properly terminated after the desired tasks have been completed
net_connect.disconnect 



