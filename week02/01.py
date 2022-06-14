# Kirk Byers Free Python Course 2022
# Week 2, exercise 1
# Jaap de Vos
#
# Open the "show_version.txt" file for reading. Use the .read() method to read
#  in the entire file contents to a variable. Print out the file contents to the screen.
# Also print out the type of the variable (you should have a string at this point).
#
# Close the file.
#
# Open the file a second time using a Python context manager (with statement).
# Read in the file contents using the .readlines() method. Print out the file contents to the screen.
# Also print out the type of the variable (you should have a list at this point).

print("#" * 100)
print("##### Printing file content 1st time")
print("#" * 100)
print("")

f = open('show_version.txt')
output = f.read()
f.close()

print("#" * 100)
print(output)
print("")
print(f"The 1st output type is: {type(output)}")
print("#" * 100)
print("")

print("#" * 100)
print("##### Printing file content 2nd time")
print("#" * 100)
print("")

with open('show_version.txt') as f:
    output = f.readlines()

print("#" * 100)
print(output)
print("")
print(f"The 2nd output type is: {type(output)}")
print("#" * 100)
print("")

