# Getting the ip address of your pc
# put on your data connection
# using command prompt: type "ipconfig" to get the ip address of the pc
import socket 
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(hostname)
print(ip_address)
