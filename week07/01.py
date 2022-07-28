# Kirk Byers Free Python Course 2022
# Week 7, exercise 1
# Jaap de Vos
#
# ## 1A ## Use Jinja2 templating to render the following:
'''
vlan
 name 
'''
# Your template should be inside of your Python program for simplicity.
# The output from processing your template should be as follows. 
# This should be printed to stdout.
'''
vlan 400
 name red400
'''
#
# ## 1B ## Using a conditional in a Jinja2 template, generate the following output:
'''
crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
'''
# The encryption of aes, and the Diffie-Hellman group should be variables
#  in the template.
# Additionally this entire ISAKMP section should only be added
#  if the isakmp_enable variable is set to True.
# Your template should be inside your Python program for simplicity.
# 
# ## 1C ## Using Jinja2 templating and a for-loop inside the template,
#  generate the following configuration snippet:
'''
vlan 501
 name blue501
vlan 502
 name blue502
vlan 503
 name blue503
vlan 504
 name blue504
vlan 505
 name blue505
vlan 506
 name blue506
vlan 507
 name blue507
vlan 508
 name blue508
'''
# Your template should be inside your Python program for simplicity.
# It is fine for your VLAN IDs to be out of order in the generated configuration
#  (for example, VLAN ID 508 can come before VLAN ID 504).

# Importing stuff
import jinja2

##### 1A #####
print("#" * 100)
print("##### 1A #####")
print("#" * 100)

vlan_template = '''
vlan {{ vlan_id }}
 name {{ vlan_name }}
'''

vlan_vars = {
    'vlan_id': '400',
    'vlan_name': 'red400'
}

template = jinja2.Template(vlan_template)
print(template.render(vlan_vars))
print("")

##### 1B #####
print("#" * 100)
print("##### 1B #####")
print("#" * 100)

isakmp_template = '''
{%- if isakmp_enabled %}
crypto isakmp policy 10
 encr aes
 authentication pre-share
 group {{ dh_group }}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{%- endif %}
'''

isakmp_vars = {
    'isakmp_enabled': True,
    'dh_group': '5'
}

template = jinja2.Template(isakmp_template)
print(template.render(isakmp_vars))
print("")

##### 1C #####
print("#" * 100)
print("##### 1C #####")
print("#" * 100)

vlan_template = '''
{%- for name, id in vlans.items() %}
vlan {{ id }}
 name {{ name }}
{%- endfor %}
'''

cfg_data = {
    'vlans': {
        'blue501': '501',
        'blue502': '502',
        'blue503': '503',
        'blue504': '504',
        'blue505': '505',
        'blue506': '506',
        'blue507': '507',
        'blue508': '508'
   }
}

template = jinja2.Template(vlan_template)
print(template.render(cfg_data))
print("")
