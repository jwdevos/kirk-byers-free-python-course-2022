# Kirk Byers Free Python Course 2022
# Week 6, exercise 1
# Jaap de Vos
#
# Using Netmiko, establish a connection to a network device and print out the device's prompt.


# Importing stuff
# from getpass import getpass
from netmiko import Netmiko
# import pdb
from pprint import pprint
# import re
    
# Printing a nice bar
print("")
print("#" * 100)
print("")

usr = 'admin'
pwd = 'admin'

fg1 = {
    'host': '192.168.108.128',
    'username': usr,
    'password': pwd,
    'device_type': 'fortinet'
}

net_conn = Netmiko(**fg1)
output = net_conn.find_prompt()
net_conn.disconnect()
print(output)

print("")
print("#" * 100)
print("")
