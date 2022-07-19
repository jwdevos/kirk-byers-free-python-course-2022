# Kirk Byers Free Python Course 2022
# Week 6, exercise 3
# Jaap de Vos
#
# Find a command on your device that has additional prompting.
# Use send_command_timing to send the command down the SSH channel.
# Capture the output and handle the additional prompting.

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
output1 = net_conn.send_command('execute reboot', expect_string=r'(y\/n)')
output2 = ''
if 'continue?' in output1:
    print(output1)
    output2 = net_conn.send_command('y')
net_conn.disconnect()
print(output2)

print("")
print("#" * 100)
print("")
