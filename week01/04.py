# Kirk Byers Free Python Course 2022
# Week 1, exercise 4
# Jaap de Vos
#
# Create a show_version variable that contains the following:
# show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
# 
# Remove all leading and trailing whitespace from the string.
# Split the string and extract the model and serial_number from it.
# Check if 'Cisco' is contained in the model string (ignore capitalization).
# Check if '881' is in the model string.
# Print out both the serial number and the model.

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
print(show_version)
print(len(show_version))
print("")

show_version_stripped = show_version.strip()
print(show_version_stripped)
print(len(show_version_stripped))
print("")

show_version_split = show_version.split()
model = show_version_split[1]
serial = show_version_split[2]

vendor = 'Cisco'
print("Model is Cisco?")
print(vendor.lower() in model.lower())
print("")

print("Model is 881?")
print('881' in model)
print("")

print("Model: " + model)
print("Serial: " + serial)


