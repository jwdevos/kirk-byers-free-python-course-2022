# Kirk Byers Free Python Course 2022
# Week 4, exercise 1
# Jaap de Vos
#
# Create a dictionary representing a network device.
# The dictionary should have key-value pairs representing
#   the 'ip_addr', 'vendor', 'username', and 'password' fields.
#
# Print out the 'ip_addr' key from the dictionary.
#
# If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'.
# If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.
#
# Create a second dictionary named 'bgp_fields'.
# The 'bgp_fields' dictionary should have a keys for 'bgp_as',
#   'peer_as', and 'peer_ip'.
#
# Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs
#   to the network device dictionary.
# 
# Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.
#
# Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.

# Importing stuff
from pprint import pprint

# Printing a nice bar
print("")
print("#" * 100)
print("")

net_dev = {}
net_dev['vendor'] = 'cisco'
net_dev['ip_addr'] = '1.2.3.4'
net_dev['username'] = 'jaap'
net_dev['password'] = 'password'

print(net_dev['ip_addr'])

if net_dev['vendor'] == 'cisco':
    net_dev['platform'] = 'ios'
elif net_dev['vendor'] == 'juniper':
    net_dev['platform'] = 'junos'

print("")

bgp_fields = {}
bgp_fields['bgp_as'] = '65321'
bgp_fields['peer_as'] = '65123'
bgp_fields['peer_ip'] = '4.3.2.1'

net_dev.update(bgp_fields)
print(net_dev)

for key in net_dev:
    print(key)

print("")

for k, v in net_dev.items():
    print(k + " = " + v)

print("")
print("#" * 100)
print("")
