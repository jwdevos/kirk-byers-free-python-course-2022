# Kirk Byers Free Python Course 2022
# Week 1, exercise 2
# Jaap de Vos
#
# Prompt a user to enter in an IP address from standard input.
# Read the IP address in and break it up into its octets.
# Print out the octets in decimal, binary, and hex.
# 
# Your program output should look like the following:
'''​
 $ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------
'''
# Four columns, fifteen characters wide, a header column, data centered in the column.

ip_addr = input("Provide an IPv4 address: ")
octects = ip_addr.split('.')

print("    Octet1         Octet2         Octet3         Octet4")
print("------------------------------------------------------------")
print(f"{octects[0]:^15}{octects[1]:^15}{octects[2]:^15}{octects[3]:^15}")
print(f"{bin(int(octects[0])):^15}{bin(int(octects[1])):^15}{bin(int(octects[2])):^15}{bin(int(octects[3])):^15}")
print(f"{hex(int(octects[0])):^15}{hex(int(octects[1])):^15}{hex(int(octects[2])):^15}{hex(int(octects[3])):^15}")
print("------------------------------------------------------------")
