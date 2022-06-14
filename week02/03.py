# Kirk Byers Free Python Course 2022
# Week 2, exercise 3
# Jaap de Vos
#
# Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.
# Use pretty print to print out the resulting list to the screen, syntax is:
'''from pprint import pprint
pprint(some_var)'''
# Use the list .sort() method to sort the list based on IP addresses.
# Create a new list slice that is only the first three ARP entries.
# Use the .join() method to join these first three ARP entries
#   back together as a single string using the newline character ('\n') as the separator.
# Write this string containing the three ARP entries out to a file named "arp_entries.txt".

# Importing stuff
from pprint import pprint

print("#" * 100)
with open('show_arp.txt') as f:
    output = f.readlines()
print("# Print the list without the header line")
pprint(output[1:])
print("")

output.sort()
print("# Print the list sorted by IP")
pprint(output)
print("")

slice = output[:3]
print("# Print a new list with a slice (first 3 lines) of the old list")
pprint(slice)
print("")

str = "\n".join(slice)
print(str)

f = open("arp_entries.txt", mode="w")
f.write(str)
f.close

