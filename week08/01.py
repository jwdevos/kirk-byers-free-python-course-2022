# Kirk Byers Free Python Course 2022
# Week 8, exercise 1
# Jaap de Vos
#
# ## 1A ## Import the 'datetime' library. Print out the module that is
#  being imported by datetime (the __file__ attribute)
#
# Import the Python ipaddress library. Print out the module that is being
#  imported by ipaddress (the __file__ attribute). If you are using
#  Python 2.7, you will need to pip install the ipaddress library.
#
# Import sys and use pprint to pprint sys.path
# 
# ## 1B ## In a separate Python file named 'my_devices.py', define a dictionary
#  named 'rtr1' with the following key-value pairs:
'''
host = rtr1.domain.com
username = cisco
password = cisco123
device_type = cisco_ios
'''
# Import my_devices into this program, and print the rtr1 dictionary
#  to the screen using pprint.
# 
# ## 1C ## In a Python shell, try importing the 'my_devices' when my_devices.py
#  is not in your current working directory.
#
# What exception do you get when you do this?
#
# Update your PYTHONPATH environment variable so that you are
#  successfully able to import this module.

# Importing stuff
import datetime
import ipaddress
import my_devices
import sys
from pprint import pprint

print(datetime.__file__)
print(ipaddress.__file__)
pprint(sys.path)
pprint(my_devices.rtr1)
