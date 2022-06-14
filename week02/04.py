# Kirk Byers Free Python Course 2022
# Week 2, exercise 4
# Jaap de Vos
#
# Read in the "show_ip_int_brief.txt" file into your program
#  using the .readlines() method.
#
# Obtain the list entry associated with the FastEthernet4 interface.
# You can just hard-code the index at this point
#  since we haven't covered for-loops or regular expressions.
# Use the string .split() method to obtain both the IP address
#  and the corresponding interface associated with the IP.
#
# Create a two element tuple from the result (intf_name, ip_address).
#
# Print that tuple to the screen.
#
# Use pycodestyle on this script. Get the warnings/errors to zero.
# You might need to 'pip install pycodestyle' on your computer
#  (you should be able to type this from the shell prompt).
# Alternatively, you can type 'python -m pip install pycodestyle'.

# Importing stuff
from pprint import pprint

# Printing a nice bar
print("#" * 100)

# Opening a file
with open('show_ip_int_brief.txt') as f:
    output = f.readlines()

# Getting the list index number for the FastEthernet4 line with hard-coded crap
f4_linenumber = output.index('FastEthernet4              10.220.88.20' +
                             '    YES NVRAM  up                    up      \n')

# Selecting the indexed line and putting it splitted in a new var
splitted_line_4 = output[f4_linenumber].split()

# Creating a tuple with some content of the splitted line var
line_4_tuple = (splitted_line_4[0], splitted_line_4[1])

# Printing the tuple
print(line_4_tuple)
