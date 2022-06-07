# Kirk Byers Free Python Course 2022
# Week 1, exercise 5
# Jaap de Vos
#
# You have the following three variables from the arp table of a router:
# mac1 = "Internet 10.220.88.29 94 5254.abbe.5b7b ARPA FastEthernet4"
# mac2 = "Internet 10.220.88.30 3 5254.ab71.e119 ARPA FastEthernet4"
# mac3 = "Internet 10.220.88.32 231 5254.abc7.26aa ARPA FastEthernet4"
#
# Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:
"""
             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa
"""
# Two columns, 20 characters wide, data right aligned, a header column.

mac1 = "Internet 10.220.88.29 94 5254.abbe.5b7b ARPA FastEthernet4"
mac2 = "Internet 10.220.88.30 3 5254.ab71.e119 ARPA FastEthernet4"
mac3 = "Internet 10.220.88.32 231 5254.abc7.26aa ARPA FastEthernet4"

print("             IP ADDR          MAC ADDRESS")
print("-------------------- --------------------")
print(f"{mac1.split()[1]:>20} {mac1.split()[3]:>20}")
print(f"{mac2.split()[1]:>20} {mac2.split()[3]:>20}")
print(f"{mac3.split()[1]:>20} {mac3.split()[3]:>20}")
