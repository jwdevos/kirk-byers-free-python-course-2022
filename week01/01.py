# Kirk Byers Free Python Course 2022
# Week 1, exercise 1
# Jaap de Vos
#
# Create a Python script that has three variables:
# ip_addr1, ip_addr2, ip_addr3 (representing three corresponding IP addresses). 
# Print these three variables to standard output using a single print statement.
#
# Make your print statement compatible with both Python2 and Python3.
#
# If you are using either Linux or MacOS make your program executable by adding a shebang line 
# and by changing the files permissions (i.e. chmod 755 exercise1.py).

ip_addr1 = '1.1.1.1'
ip_addr2 = '2.2.2.2'
ip_addr3 = '3.3.3.3'

print(f"{ip_addr1:^20}{ip_addr2:^20}{ip_addr3:^20}")
