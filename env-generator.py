#! /usr/bin/env python

# This script will generate a ~/.parc file to store power platform environment credentials
#
# Usage: python env-generator.py -s <section_name>

import sys, os
import re
import argparse
import ConfigParser
from os.path import expanduser


parser = argparse.ArgumentParser(description='Use the applicationid and secret of an app registered in AAD and tied to an application user in the target power platform environment')
parser.add_argument('--config_section', '-s', action='store',
	help='create new config section with this section name.')
args= parser.parse_args()

print("Power Platform Environment File Generator")
print("This script generates a ~/.parc file to store power platform environment credentials\n")
print("After creating an app registration in azure id and adding it as an application user in the")
print("target power platform environment, paste credentials int following format after the prompt and then press enter")
print("name: [SECTION_NAME] tenant: [TENANT] key: [CLIENT-ID] secret: [CLIENT-SECRET] resource: [ENVIRONMENT-URL]\n")
print("e.g. name: dev-contoso tenant: contoso.onmicrosoft.com key: highlyconfenditialkey secret: highlyconfidentialsecret resource: https://dev-contoso.crm.dynamics.com")

sys.stdout.write('>>>\n')
text = sys.stdin.readline()
sys.stdout.write('<<<\n\n')

# load the cred data
home = expanduser("~")
fieldlist = text.split()
index = 0
fields = {}

# Parse the cred data
while index < len(fieldlist):
	print(fieldlist[index])
	if (re.search(r':$', fieldlist[index])):
		fields[fieldlist[index]] = fieldlist[index + 1]
	index += 1


print(fields)

# Determine the section name giving precedence to -s value
if args.config_section:
	section_name = args.config_section
	section_name_pretty = args.config_section
else:
	section_name = fields['name:']
	section_name_pretty = fields['name:']
	print("+++ Found client credentials with the name: %s" % section_name)

# Fix up default sections
if section_name.lower() == "default":
	section_name = "----DEFAULT----"
	section_name_pretty = "default"

# Process the original .parc file
origConfig = ConfigParser.ConfigParser()
filename = "%s/.parc" % home

# If this is a new file, create it
if not os.path.isfile(filename):
	print("+++ Creating new credentials file: %s" % filename)
	open(filename, 'a+').close()
else:
	print("+++ Found credentials file: %s" % filename)

# Recommend default section name if not present
origConfig.read(filename)
if 'default' not in origConfig.sections():
	reply = str(raw_input('\nThere is no default section in ~/.parc, do you want to use these credentials as default? [y/n]: ')).lower().strip()
	print("")
	if reply[0] == 'y':
		section_name = "----DEFAULT----"
		section_name_pretty = "default"

if section_name_pretty in origConfig.sections():
	print(">>> Replacing section: %s" % section_name_pretty)
	replace_section = True
else:
	print("+++ Creating section: %s" % section_name_pretty)
	replace_section = False

# Make sure that this is ok ~ any key to continue
try:
	input("\nPress Enter to continue or ctrl-c to exit.")
except SyntaxError:
	pass

# We need a line for the output to look nice
print

# If we have a 'default' section hide it from ConfigParser
with open(filename, "r+") as myfile:
	data = myfile.read().replace('default', '----DEFAULT----')
	myfile.close()
with open (filename, "w") as myfile:
	myfile.write(data)
	myfile.close()

# Open the ~/.parc file for writing
Config = ConfigParser.ConfigParser()
Config.read(filename)
configfile = open(filename,'w')

# Remove a section that is being replaced
if replace_section:
	print("--- Removing section: %s" % section_name_pretty)
	Config.remove_section(section_name)

# Add the new section
print("+++ Adding section: %s" % section_name_pretty)
Config.add_section(section_name)
Config.set(section_name,'tenant',fields['tenant:'])
Config.set(section_name,'key',fields['key:'])
Config.set(section_name,'secret',fields['secret:'])
Config.set(section_name,'resource',fields['resource:'])

Config.write(configfile)

configfile.close()

# Undo the ConfigParser work around
with open (filename, "r") as myfile:
	data=myfile.read().replace('----DEFAULT----','default')
	myfile.close()
with open (filename, "w") as myfile:
	myfile.write(data)
	myfile.close()

print("\nDone. Please verify your credentials with the verify_creds.py script.")
print
