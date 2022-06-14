# Kirk Byers Free Python Course 2022
# Week 2, exercise 5
# Jaap de Vos
#
# Read the 'show_ip_bgp_summ.txt' file into your program.
#  From this BGP output obtain the first and last lines of the output.
# From the first line use the string .split() method
#  to obtain the local AS number.
# From the last line use the string .split() method
#  to obtain the BGP peer IP address.
# Print both local AS number and the BGP peer IP address to the screen.

# Printing a nice bar
print("#" * 100)

# Opening a file
with open('show_ip_bgp_summ.txt') as f:
    output = f.readlines()

# Getting the first line, splitting and selecting the last item
first_line = output[0]
print(f"Local AS: {first_line.split()[-1]}")

# Getting the last line, splitting and selecting the first item
last_line = output[-1]
print(f"Peer IP: {last_line.split()[0]}")
