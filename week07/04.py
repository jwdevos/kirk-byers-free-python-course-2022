# Kirk Byers Free Python Course 2022
# Week 7, exercise 4
# Jaap de Vos
#
# Take the YAML file and corresponding data structure that you defined in exercise3b:
'''
{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}
'''
# From this YAML data input source, use Jinja templating to
#  generate the following configuration output:
'''
interface Ethernet1
  switchport mode access
  switchport access vlan 10
interface Ethernet2
  switchport mode access
  switchport access vlan 20
interface Ethernet3
  switchport mode trunk
  switchport trunk native vlan 1
  switchport trunk allowed vlan all
'''
# The following should all be variables in your Jinja template
#  (the names may be different than below, but they should be
#  variabilized and not be hard-coded in your template).
'''
interface_name
switchport_mode
access_vlan
native_vlan
trunk_vlans
'''
# All your Jinja2 variables should be retrieved from your YAML file.
# This exercise might be challenging.

# Importing stuff
import jinja2
import yaml
from pprint import pprint

filename = '04.yml'
with open(filename) as f:
    output = yaml.load(f, Loader=yaml.SafeLoader)
template_vars = output

#pprint(template_vars)
#print("")

input_template = '04.j2'
with open(input_template) as f:
   read_template = f.read()

template = jinja2.Template(read_template)
print(template.render(template_vars))
