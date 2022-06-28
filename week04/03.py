# Kirk Byers Free Python Course 2022
# Week 4, exercise 3
# Jaap de Vos
#
#  Read in the 'show_version.txt' file. From this file,
#   use regular expressions to extract the OS version,
#   serial number, and configuration register values.
# Your output should look as follows:
'''
OS Version: 15.4(2)T1
Serial Number: FTX0000038X
​Config Register: 0x2102
'''

# Importing stuff
from pprint import pprint
import re

# Printing a nice bar
print("")
print("#" * 100)
print("")

net_dev = {}

# Opening a file
with open('show_version.txt') as file:
    output = file.read()

net_dev['version'] = re.search(r"Version (\S+),", output).group(1)
net_dev['serial'] = re.search(r"Processor board ID (\S+)", output).group(1)
net_dev['conf_reg'] = re.search(r"Configuration register is (\S+)", output).group(1)

print("")

print(f"OS Version: {net_dev['version']}")
print(f"Serial Number: {net_dev['serial']}")
print(f"​Config Register: {net_dev['conf_reg']}")

print("")
print("#" * 100)
print("")
