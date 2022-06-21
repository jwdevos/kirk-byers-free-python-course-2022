# Kirk Byers Free Python Course 2022
# Week 3, exercise 1
# Jaap de Vos
#
# Read the "show_vlan.txt" file into your program.
# Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations.
# From these VLAN_ID and VLAN_NAME construct a new list where each element in the list
#  is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen.
# Your output should look as follows:
'''
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
'''

# Importing stuff
from pprint import pprint

# Printing a nice bar
print("#" * 100)

# Opening a file
with open('show_vlan.txt') as file:
    output = file.readlines()[2:]

outputlist = []

for line in output:
    tmp = line.split()
    if tmp[0][0].isdigit():
        tmp_tuple = (tmp[0], tmp[1])
        outputlist.append(tmp_tuple)

pprint(outputlist)
