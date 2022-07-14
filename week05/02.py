# Kirk Byers Free Python Course 2022
# Week 5, exercise 2
# Jaap de Vos
#
# Create a function that randomly generates an IP address for a network.
# The default base network should be '10.10.10.'.
# For simplicity the network will always be a /24.
#
# You should be able to pass a different base network into your function as an argument.
# Randomly pick a number between 1 and 254 for the last octet and return the full IP address.
# You can use the following to randomly generate the last octet:
'''
import random
random.randint(1, 254)
'''
# Call your function using no arguments.
# Call your function using a positional argument.
# Call your function using a named argument.
#
# For each function call print the returned IP address to the screen.

# Importing stuff
from pprint import pprint
import random

def random_ip(base_net='10.10.10.'):
    rint = random.randint(1, 254)
    print(f"{base_net}{rint}")
    print("")

# Printing a nice bar
print("")
print("#" * 100)
print("")

print("##### Calling the function without argument #####")
random_ip()

print("##### Calling the function positional argument #####")
random_ip('192.168.1.')

print("##### Calling the function named argument #####")
random_ip(base_net='172.16.255.')

print("")
print("#" * 100)
print("")
