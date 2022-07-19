# Kirk Byers Free Python Course 2022
# Week 6, exercise 4
# Jaap de Vos
#
# Use send_config_set() and send_config_from_file()
#  to make configuration changes.
# The configuration changes should be benign.
#  For example, on Cisco IOS I typically change the logging buffer size.
# As part of your program verify that the configuration change occurred properly.
#  For example, use send_command() to execute 'show run' and verify the new configuration.

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

# Defining some vars
usr = 'admin'
pwd = 'admin'
timeout = 410

# Defining a dir with Netmiko required parameters for a device
fg1 = {
    'host': '192.168.108.128',
    'username': usr,
    'password': pwd,
    'device_type': 'fortinet'
}

# Making a Netmiko object for the device in the dir
net_conn = Netmiko(**fg1)

# Making a list of commands to send
cfg_commands = ['config system global', 'set admintimeout {}'.format(timeout), 'end']

# Getting the current admintimeout
print("##### Getting the current admintimeout #####")
output = net_conn.send_command('get system global | grep admintimeout')
print(output)

# Sending the command list, changing the timeout
print("##### Changing the admintimeout ######")
output = net_conn.send_config_set(cfg_commands)
print(output)

# Getting the admintimeout again
print("##### Getting the admintimeout again #####")
output = net_conn.send_command('get system global | grep admintimeout')
print(output)

# Getting the current port2 info
print("##### Getting the current port2 info #####")
output = net_conn.send_command('get system interface | grep port2')
print(output)

# Setting a static IP on port2
print("##### Setting a static IP on port2 ######")
output = net_conn.send_config_from_file('cfg.txt')

# Getting the port2 info again
print("##### Getting the port2 info again #####")
output = net_conn.send_command('get system interface | grep port2')
print(output)

net_conn.disconnect()

print("")
print("#" * 100)
print("")
