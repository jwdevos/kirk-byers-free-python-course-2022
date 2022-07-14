# Kirk Byers Free Python Course 2022
# Week 5, exercise 4
# Jaap de Vos
#
# Copy your solution from exercise3 to exercise4.
# Add an 'import pdb' and pdb.set_trace() statement outside of
#  your function (i.e. where you have your function calls).
#
# Inside of pdb, experiment with:
# - Listing your code.
# - Using 'next' and 'step' to walk through your code.
#   - Make sure you understand the difference between next and step.
# - Experiment with 'up' and 'down' to move up and down the code stack.
# - Use p <variable> to inspect a variable.
# - Set a breakpoint and run your code to the breakpoint.
# - Use '!command' to change a variable (for example !new_mac = [])

# Importing stuff
import pdb
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
pdb.set_trace()
sanitize_mac(input_mac)

print("##### Sanitizing a dotted MAC #####")
input_mac = '0000.aaaa.bbbb'
pdb.set_trace()
sanitize_mac(input_mac)

print("##### Sanitizing a single digit MAC #####")
input_mac = 'a:b:c:d:e:f'
pdb.set_trace()
sanitize_mac(input_mac)

print("")
print("#" * 100)
print("")
