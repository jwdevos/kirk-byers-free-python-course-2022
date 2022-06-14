# Kirk Byers Free Python Course 2022
# Week 2, exercise 2
# Jaap de Vos
#
# Create a list of five IP addresses.
# Use the .append() method to add an IP address onto the end of the list.
# Use the .extend() method to add two more IP addresses to the end of the list.
# Use list concatenation to add two more IP addresses to the end of the list.
# Print out the entire list of ip addresses.
#  Print out the first IP address in the list. Print out the last IP address in the list.
# Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
# Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.

print("#" * 100)
ips = ['1.1.1.1', '1.1.1.2', '1.1.1.3', '1.1.1.4', '1.1.1.5']
print("# Printing the new list of IP's")
print(ips)
print("")

ips.append('1.1.1.6')
print("# Printing the list with an appended IP")
print(ips)
print("")

ips.extend(['1.1.1.7', '1.1.1.8'])
print("# Printing the extended list")
print(ips)
print("")

ips = ips + ['1.1.1.9', '1.1.1.10.']
print("# Printing the concatenated list")
print(ips)
print("")

print(f"The first IP of the list: {ips[0]}")
print(f"The first IP of the list: {ips[-1]}")
print("")

ips.pop(0)
ips.pop()
print("# Printing the popped list")
print(ips)
print("")

ips[0] = '2.2.2.2'
print("# Printing the list with a new first IP")
print(ips)
print("")

