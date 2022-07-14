# Kirk Byers Free Python Course 2022
# Week 5, exercise 3
# Jaap de Vos
#
# Write a function that normalizes a MAC address to the following format:
# 01:23:45:67:89:AB
#
# This function should handle the lower-case to upper-case conversion.
# It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
# The function should have one parameter, the mac_address. It should return the normalized MAC address
#
# Single digit bytes should be zero-padded to two digits. In other words, this:
# a:b:c:d:e:f should be converted to: 0A:0B:0C:0D:0E:0F
#
# Write several test cases for your function and verify it is working properly.

# Importing stuff
from pprint import pprint
import re

def sanitize_mac(raw_mac):
    cased_raw_mac = raw_mac.upper()

    dash_pattern = re.compile("^..-..-..-..-..-..")
    dot_pattern = re.compile("^....\.....\.....")
    single_pattern = re.compile("^.:.:.:.:.:.")

    if dash_pattern.match(cased_raw_mac):
        sanitized_mac = cased_raw_mac.replace('-', ':')
        print(sanitized_mac)
    elif dot_pattern.match(cased_raw_mac):
        sanitized_mac = (cased_raw_mac[:2] + ':' +
                     cased_raw_mac[2:4] + ':' +
                     cased_raw_mac[5:7] + ':' +
                     cased_raw_mac[7:9] + ':' +
                     cased_raw_mac[10:12] + ':' +
                     cased_raw_mac[12:14])
        print(sanitized_mac)
    elif single_pattern.match(cased_raw_mac):
        sanitized_mac = (
            '0' + cased_raw_mac[0] + ':' +
            '0' + cased_raw_mac[2] + ':' +
            '0' + cased_raw_mac[4] + ':' +
            '0' + cased_raw_mac[6] + ':' +
            '0' + cased_raw_mac[8] + ':' +
            '0' + cased_raw_mac[10]
        )
        print(sanitized_mac)
    else:
        print("INVALID INPUT - GET A NEW BRAIN")
    
    print("")
    
# Printing a nice bar
print("")
print("#" * 100)
print("")

print("##### Sanitizing a dashed MAC #####")
input_mac = '00-00-aa-aa-bb-bb'
sanitize_mac(input_mac)

print("##### Sanitizing a dotted MAC #####")
input_mac = '0000.aaaa.bbbb'
sanitize_mac(input_mac)

print("##### Sanitizing a single digit MAC #####")
input_mac = 'a:b:c:d:e:f'
sanitize_mac(input_mac)

print("")
print("#" * 100)
print("")
