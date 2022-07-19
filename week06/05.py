# Kirk Byers Free Python Course 2022
# Week 6, exercise 5
# Jaap de Vos
#
# Use send_command() in conjunction with ntc-templates
#  to execute a show command. Have TextFSM automatically convert
#  this show command output to structured data.se send_command()
#  to send a show command down the SSH channel.
# Retrieve the results and print the results to the screen.

# Importing stuff
# from getpass import getpass
import logging
from netmiko import Netmiko
# import pdb
from pprint import pprint
# import re

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')

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
output = net_conn.send_command('get system arp', use_textfsm=True)
net_conn.disconnect()
print(output)

print("")
print("#" * 100)
print("")
