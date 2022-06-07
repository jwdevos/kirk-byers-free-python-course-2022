# Kirk Byers Free Python Course 2022
# Week 1, exercise 3
# Jaap de Vos
#
# Create three different variables.
# The first variable should use all lower case characters with underscore ( _ ) as the word separator.
# The second variable should use all upper case characters with underscore as the word separator.
# The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.
# 
# Make all three variables be strings that refer to IPv6 addresses.
# 
# Use the from future technique so that any string literals in Python2 are unicode.
# 
# compare if variable1 equals variable2
# compare if variable1 is not equal to variable3

this_is_var_one = '2001:4860:4860::8888'
THIS_IS_VAR_TWO = '2001:4860:4860::8844'
this_is_VAR_3   = '2606:4700:4700:0:0:0:0:64'

print(this_is_var_one is THIS_IS_VAR_TWO)
print(this_is_var_one is not this_is_VAR_3)
