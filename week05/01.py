# Kirk Byers Free Python Course 2022
# Week 5, exercise 1
# Jaap de Vos
#
# 1a. Create an ssh_conn function.
# This function should have three parameters:
#   ip_addr, username, and password.
# The function should print out each of these three variables
#  and clearly indicate which variable it is printing out.
#
# Call this ssh_conn function using entirely positional arguments.
# Call this ssh_conn function using entirely named arguments.
# Call this ssh_conn function using a mix of positional and named arguments.
# 
# 1b. Expand on the ssh_conn function from exercise1
#  except add a fourth parameter 'device_type' with a default value
#  of 'cisco_ios'. Print all four of the function variables out
#  as part of the function's execution.
# Call the 'ssh_conn2' function both with and without specifying the device_type
# Create a dictionary that maps to the function's parameters.
# Call this ssh_conn2 function using the **kwargs technique.

# Importing stuff
from pprint import pprint

def ssh_conn(ip_addr, username, password, device_type='cisco_ios'):
    print(f"ip_addr: {ip_addr}")
    print(f"username: {username}")
    print(f"password: {password}")
    print(f"device_type: {device_type}")
    print("")

# Printing a nice bar
print("")
print("#" * 100)
print("")

print("##### Calling the function with only positional arguments #####")
ssh_conn('10.1.1.1', 'usr', 'pass')

print("##### Calling the function with only named arguments #####")
ssh_conn(ip_addr='10.1.1.1', username='usr', password='pass')

print("##### Calling the function with positional and named arguments #####")
ssh_conn('10.1.1.1', 'usr', password='pass', device_type='junos')

print("##### Calling the function with arguments from dictionary #####")
dev = {
    'ip_addr': '1.10.10.10',
    'username': 'rsu',
    'password': 'pss',
    'device_type': 'arista'
}
ssh_conn(**dev)


print("")
print("#" * 100)
print("")
