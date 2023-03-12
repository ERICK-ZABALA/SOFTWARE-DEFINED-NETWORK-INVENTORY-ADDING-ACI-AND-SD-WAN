#!/home/codespace/.python/current/bin/python3

import argparse
from getpass import getpass
from pyats.topology.loader import load

# Plan for adding ACI and SD-WAN to inventory
# Steps:
# 1. Additional arguments for ACI and SD-WAN Controllers
#    - Optional arguments for address of each controller
# 2. Request credentials for if needed
#    - Use Python "input()" function
# 3. Make REST API cals to gather inventory details
#    - After functions that parse commands for CLI 
#      devices
# 4. Add to network inventory
#    - Mantain same tuple based format from CLI devices
#      (device_name,device_os, software_version, uptime, serial_number)
#    - For device os use "controller-model" format

# Use argparse to determine the testbed file:
# https://docs.python.org/3/library/argparse.html

def lookup_aci_info(aci_address, aci_username, aci_password):
    """
    Use REST API for ACI to lookup and return details
    In case of an error, return False.
    """

    # Authenticate to API
    # Send API Request(s) for information
    # Compile and return information

    return False


parser = argparse.ArgumentParser(description='Generate network inventory report from testbed')
parser.add_argument('testbed', type=str, help='pyATS Testbed File')
parser.add_argument('--aci-address', type=str, help='Cisco ACI Controller address for gathering inventory details')
parser.add_argument('--sdwan-address', type=str, help='Cisco SD-WAN Controller address for gathering inventory details')
args = parser.parse_args()

# Create pyATS testbed object
print(f'Loading testbed file {args.testbed}')
testbed = load(args.testbed)

#Check if ACI and/or SD-WAN address provided
if args.aci_address:
    print(f"\n\033[94mInventory details will be pulled from Cisco APIC {args.aci_address}\033[0m")
    aci_username = input(f'What is the username for {args.aci_address}? ')
    aci_password = getpass(f'What is the password for {args.aci_address}? (input will be hidden)')
    print()


if args.sdwan_address:
    print(f'\033[94mInvntory details will be pulled from Cisco SD-WAN Controller {args.sdwan_address}\n\033[0m')
    sdwan_username = input(f"What is the username for {args.sdwan_address}? ")
    sdwan_password = getpass(f"What is the password for {args.sdwan_address}? (input will be hidden)")
    print()

# Gathering info on inventory from ACI and SD-WAN
if args.aci_address:
    print(f"Inventory details will be pulled from Cisco APIC {args.aci_address}")
    aci_info = lookup_aci_info(args.aci_address, aci_username, aci_password)
    
    # for debug, print results
    print(aci_info)

if args.sdwan_address:
    print(f"Inventory details will be pulled from Cisco APIC {args.sdwan_address}")
    sdwan_info = lookup_aci_info(args.sdwan_address, sdwan_username, sdwan_password)
    
    # for debug, print results
    print(sdwan_info)




