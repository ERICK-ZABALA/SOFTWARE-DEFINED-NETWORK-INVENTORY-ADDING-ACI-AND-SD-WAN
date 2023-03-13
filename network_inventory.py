#!/home/devnet/Documents/SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN/sdn/bin/python

import argparse
from getpass import getpass
from pyats.topology.loader import load
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

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

def auth_aci(aci_address, aci_username, aci_password):
    """Retrieve Authentication Token from ACI Controller"""
    # The API Endpoint for authentication
    url = f"https://{aci_address}/api/aaaLogin.json"

    # The data payload for authentication
    payload = {"aaaUser": {"attributes":{"name": aci_username,
                                         "pwd": aci_password}}} 
    # Send the request to the controller
    try:
        response = requests.post(url, json=payload, verify=False)

        # If the request succeeded, return the token
        if response.status_code == 200:
            return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
        else:
            return False
    
    except Exception as e:
        print(" Error: Unable to authentication to APIC")
        print(e)
        return False


def lookup_aci_info(aci_address, aci_username, aci_password):
    """
    Use REST API for ACI to lookup and return details
    In case of an error, return False.
    """

    # Authenticate to API
    token = auth_aci(aci_address, aci_username, aci_password)
    # For debug print token value
    print(f"aci_token: {token}")
    if not token:
        print(f" Error: Unable to authenticate to {aci_address}.")

    # Send API Request(s) for information
    # Put token into cookie dict for requests
    cookies = {"API-cookie": token}
    # List to hold data for each device from controller
    inventory = []
    # Send API Request(s) for information
    # API URLs
    node_list_url = f"https://{aci_address}/api/node/class/fabricNode.json"
    node_firmware_url = "https://{aci_address}/api/node/class/{node_dn}/firmwareRunning.json"
    node_system_url = "http://{aci_address}/api/node/mo/{node_dn}.json?query-target=children&target-subtree-class=topSystem"
    # Lookup Node List from controller
    node_list_rsp = requests.get(node_list_url, cookies=cookies, verify=False)

    # For debug, print response details
    print(f"node_list_rsp status_code: {node_list_rsp.status_code}")
    print(f"node_list_rsp body: {node_list_rsp.text}")

    if node_list_rsp.status_code != 200:
        print(f" Error looking up node list from APIC. Status Code was {node_list_rsp.status_code}")
        return False
    # Loop over nodes
    fabric_nodes = node_list_rsp.json()["imdata"]
    
    for node in fabric_nodes:
        # Pull information on mode from list
        node_name = node["fabricNode"]["attributes"]["name"]
        node_model = node["fabricNode"]["attributes"]["model"]
        node_serial = node["fabricNode"]["attributes"]["serial"]
        # Lookup Firmware info with API
        
        node_software = None
        # Lookup Uptime info with API
        node_uptime = None
        # Compile and return information
        inventory.append ((node_name, f"apic-{node_model}", node_software, node_uptime, node_serial))
    
    return inventory
    

    
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




