# Kirk Byers Free Python Course 2022
# Week 4, exercise 2
# Jaap de Vos
#
# Create three separate lists of IP addresses. The first list should be
#   the IP addresses of the Houston data center routers,
#   and it should have over ten RFC1918 IP addresses in it
#   (including some duplicate IP addresses).
#
# The second list should be the IP addresses
#   of the Atlanta data center routers, and it should have
#   at least eight RFC1918 IP addresses
#   (including some addresses that overlap with the Houston data center).
#
# The third list should be the IP addresses of the Chicago data center routers,
#   and it should have at least eight RFC1918 IP addresses.
#   The Chicago IP addresses should have some overlap with
#   both the IP addresses in Houston and Atlanta.
#
# Convert each of these three lists to a set.
#
# Using a set operation, find the IP addresses that are
#   duplicated between Houston and Atlanta.
#
# Using set operations, find the IP addresses that are
#   duplicated in all three sites.
#
# Using set operations, find the IP addresses that are
#   entirely unique in Chicago.

# Importing stuff
from pprint import pprint

# Printing a nice bar
print("")
print("#" * 100)
print("")

houston_ips = ['10.1.0.1', '10.1.0.2', '10.1.0.3', '10.1.0.4', '10.1.0.5', '10.1.0.6',
               '10.1.0.7', '10.1.0.8', '10.1.0.1', '10.1.0.2']
atlanta_ips = ['10.2.0.1', '10.2.0.2', '10.1.0.3', '10.1.0.4', '10.2.0.5', '10.2.0.6',
               '10.2.0.7', '10.2.0.8', '10.2.0.9', '10.2.0.10']
chicago_ips = ['10.3.0.1', '10.3.0.2', '10.1.0.3', '10.1.0.5', '10.2.0.5', '10.2.0.6',
               '10.3.0.7', '10.3.0.8', '10.3.0.9', '10.3.0.10']
print("houston_ips: " + str(houston_ips))
print("atlanta_ips: " + str(atlanta_ips))
print("chicago_ips: " + str(chicago_ips))
print("")

houston_set = set(houston_ips)
atlanta_set = set(atlanta_ips)
chicago_set = set(chicago_ips)

print(houston_set & atlanta_set)
print(houston_set & atlanta_set & chicago_set)
print(chicago_set - houston_set - atlanta_set)

print("")
print("#" * 100)
print("")
