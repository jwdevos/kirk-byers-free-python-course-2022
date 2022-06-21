# Kirk Byers Free Python Course 2022
# Week 3, exercise 2
# Jaap de Vos
#
# Read the contents of the "show_arp.txt" file.
# Using a for loop, iterate over the lines of this file.
# Process the lines of the file and separate out
#  the ip_addr and mac_addr for each entry into a separate variable.
#
# Add a conditional statement that searches
#  for '10.220.88.1'. If 10.220.88.1 is found,
#  print out the string "Default gateway IP/Mac"
#  and the corresponding IP address and MAC Address.
#
# Using a conditional statement, also search for '10.220.88.30'.
# If this IP address is found, then print out "Arista3 IP/Mac is"
#  and the corresponding ip_addr and mac_addr.
#
# Keep track of whether you have found both the Default Gateway
#  and the Arista3 switch. Once you have found both of these devices,
#  'break' out of the for loop.

# Importing stuff
from pprint import pprint

# Printing a nice bar
print("")
print("#" * 100)
print("")

# Opening a file
with open('show_arp.txt') as file:
    output = file.readlines()[1:]

gw_flag = False
arista_flag = False

for line in output:
    split = line.split()
    ip = split[1]
    mac = split[3]
    
    if ip == '10.220.88.1':
        print(f"Default gateway IP/Mac: {ip} / {mac}")
        gw_flag = True

    
    if ip == '10.220.88.30':
        print(f"Arista3 IP/Mac: {ip} / {mac}")
        arista_flag = True

    if gw_flag and arista_flag:
        break

print("")
print("#" * 100)
print("")
