# Kirk Byers Free Python Course 2022
# Week 4, exercise 5
# Jaap de Vos
#
# Read the 'show_ipv6_intf.txt' file.
# From this file, use Python regular expressions to extract the two IPv6 addresses.
# The two relevant IPv6 addresses you need to extract are:
#   2001:11:2233::a1/24
#   2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
#
# Try to use re.DOTALL flag as part of your search.
# Your search pattern should not include any of the literal characters in the IPv6 address.
# 
# From this, create a list of IPv6 addresses that includes only the above two addresses.
# Print this list to the screen. 


# Importing stuff
from pprint import pprint
import re

# Printing a nice bar
print("")
print("#" * 100)
print("")

ipv6_list = []

# Opening a file
with open('show_ipv6_intf.txt') as file:
    output = file.read()

match =  re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet", output, flags=re.DOTALL).group(1)
match_split = match.split()
ipv6_list.append(match_split[0])
ipv6_list.append(match_split[2])
print(ipv6_list)

print("")
print("#" * 100)
print("")
