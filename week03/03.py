# Kirk Byers Free Python Course 2022
# Week 3, exercise 3
# Jaap de Vos
#
# Read the 'show_lldp_neighbors_detail.txt' file.
# Loop over the lines of this file. Keep reading the lines
#  until you have encountered the remote "System Name"
#  and remote "Port id".
# 
# Save these two items into variables and print them to the screen.
# You should extract only the system name and port id from the lines
#  (i.e. your variables should only have 'twb-sf-hpsw1' and '15').
# Break out of your loop once you have retrieved these two items.

# Importing stuff
from pprint import pprint

# Printing a nice bar
print("")
print("#" * 100)
print("")

# Opening a file
with open('show_lldp_neighbors_detail.txt') as file:
    output = file.readlines()[1:]

system_name = ''
port_id = ''
port_flag = False
system_flag = False

for line in output:
    if 'System Name' in line:
        system_name = line.split()[2]
        system_flag = True

    if 'Port id' in line:
        port_id = line.split()[2]
        port_flag = True

    if system_flag and port_flag:
        break
    
print(f"System name: {system_name}")
print(f"Port ID: {port_id}")

print("")
print("#" * 100)
print("")
