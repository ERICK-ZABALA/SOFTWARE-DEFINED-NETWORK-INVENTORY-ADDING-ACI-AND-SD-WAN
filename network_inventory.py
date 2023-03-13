#!/home/devnet/Documents/SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN/sdn/bin/python

import argparse
from getpass import getpass
from pyats.topology.loader import load
from urllib3 import disable_warnings, exceptions
import requests
from datetime import datetime
import csv

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

    payload = {
        "aaaUser": {
            "attributes":{
                "name": aci_username,
                "pwd": aci_password}
                }
            } 
    header = {
      "Content-Type" : "application/json"
   }
    # Send the request to the controller
    try:
        response = requests.post(url, headers=header, json=payload, verify=False)
        # If the request succeeded, return the token
        if response.status_code == 200:
            return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
        else:
            return False
    
    except Exception as e:
        print(" Error: Unable to authentication to APIC")
        print(e)
        return False

def auth_sdwan(sdwan_address, sdwan_username, sdwan_password):
    #The API Endpoint for authentication
    url = f"https://{sdwan_address}/j_security_check"
    # The data payload for authentication
    payload = {"j_username":sdwan_username,
               "j_password":sdwan_password }
    headers = {"Content-Type":"application/x-www-form-urlencoded"}

    try:
        response = requests.post(url, data=payload, headers=headers, verify=False)
        if response.status_code == 200 and "JSESSIONID" in response.cookies:
            return response.cookies["JSESSIONID"]
        else:
            return False
    except Exception as e:
        print("Error: Unable to authentication to SDWAN")
        print(e)
        return False

def logout_sdwan(sdwan_address, token):
    """
    Logout of SD-WAN API
    """
    # The API Endpoints for authentication
    url = f"https://{sdwan_address}/logout?nocache=15"
    # Auth Cookie
    cookies = {"JSESSIONID": token}

    # Send the request to the controller

    try:
        response = requests.get(url, cookies=cookies, verify=False)
        # Test logout
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(" Error: unable to logout from SD-WAN")
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
    cookie = {"APIC-cookie": token}
    # List to hold data for each device from controller
    inventory = []
    # Send API Request(s) for information
    # API URLs
    node_list_url = f"https://{aci_address}/api/node/class/fabricNode.json"
    node_firmware_url = "https://{aci_address}/api/node/class/{node_dn}/firmwareRunning.json"
    node_system_url = "https://{aci_address}/api/node/mo/{node_dn}.json?query-target=children&target-subtree-class=topSystem"
    # Lookup Node List from controller
    node_list_rsp = requests.get(node_list_url, cookies=cookie, verify=False)

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
        node_firmware_rsp = requests.get(node_firmware_url.format(aci_address=aci_address, node_dn=node["fabricNode"]["attributes"]["dn"]), cookies=cookie, verify=False)
        # For debug, print response details
        print(f"node_firmware_rsp status_code: {node_firmware_rsp.status_code}")
        print(f"node_firmware_rsp body: {node_firmware_rsp.text}")

        if node_firmware_rsp.status_code == 200:
            if node_firmware_rsp.json()["totalCount"] == "1":
                node_software = node_firmware_rsp.json()["imdata"][0]["firmwareRunning"]["attributes"]["version"]
            else:
                node_software = "Unknown"    
        else:
            node_software = "Error"

        #node_software = None
        # Lookup Uptime info with API
        node_system_url = "https://{aci_address}/api/node/mo/{node_dn}.json?query-target=children&target-subtree-class=topSystem"
        node_system_rsp = requests.get(node_system_url.format(aci_address=aci_address, node_dn=node["fabricNode"]["attributes"]["dn"]), cookies=cookie, verify=False)

        # For debug, print response details
        print(f"node_system_rsp status_code: {node_system_rsp.status_code}")
        print(f"node_system_rsp body: {node_system_rsp.text}")

        if node_system_rsp.status_code == 200:
            if node_system_rsp.json()["totalCount"] == "1":
                node_uptime = node_system_rsp.json()["imdata"][0]["topSystem"]["attributes"]["systemUpTime"]
                node_uptime = node_uptime.split(":")
                node_uptime = f"{node_uptime[0]} days, {node_uptime[1]} hours, {node_uptime[2]} mins"

            else:
                node_uptime = "Unknown"    
        else:
            node_uptime = "Error"

        
        # node_uptime = None
        # Compile and return information
        inventory.append ((node_name, f"apic-{node_model}", node_software, node_uptime, node_serial))
    
    return inventory
    

def lookup_sdwan_info(sdwan_address, sdwan_username, sdwan_password):
    """
    Use REST API for SDWAN to lookup and return incentory
    In case of an error, return False.
    """

    # Authentication to API
    token = auth_sdwan(sdwan_address, sdwan_username, sdwan_password)
    print(f"sdwan_token: {token}")

    if not token:
        print(f" Error: Unable to authenticate to {sdwan_address}.")
        return False
    
    # Put token into cookie dict for request
    cookies = {"JSESSIONID": token}
    
    # Send API Request for information
    device_url = f"https://{sdwan_address}/dataservice/device"
    device_rsp = requests.get(device_url, cookies=cookies, verify=False)
    # List to hold data for each  device from controller
    inventory = []
    # Loop over devices and return results
    sdwan_nodes = device_rsp.json()["data"]
    for node in sdwan_nodes:
        # Pull info on node
        node_name = node["host-name"]
        node_model = node["device-model"]
        node_serial = node["board-serial"]
        node_software = node["version"]
        uptime_date = node["uptime-date"]
        # Need to Unix TimeStamp from milliseconds to seconds
        uptime_date = datetime.fromtimestamp(uptime_date/1000)
        now = datetime.now()
        uptime_delta = now - uptime_date
        # Get days, hours, minute details
        uptime_days = uptime_delta.days
        uptime_minutes_total = int(uptime_delta.seconds / 60)
        uptime_hours = int(uptime_minutes_total / 60)
        uptime_minutes = uptime_minutes_total % 60

        node_uptime = f"{uptime_days} days, {uptime_hours} hours, {uptime_minutes} minutes"

        inventory.append((node_name, f"sdwan-{node_model}", node_software, node_uptime, node_serial))

    # For debugging, printn response
    print(f"device_rsp status_code: {device_rsp.status_code}")
    print(f"device_rsp body: {device_rsp.text}")

    # Logout API
    logout_sdwan(sdwan_address, token)
    
    # Compile and return information

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
    aci_username = "admin"
    aci_password = getpass(f'What is the password for {args.aci_address}? (input will be hidden)')
    aci_password = "C1sco12345"
    print()


if args.sdwan_address:
    print(f'\033[94mInvntory details will be pulled from Cisco SD-WAN Controller {args.sdwan_address}\n\033[0m')
    sdwan_username = input(f"What is the username for {args.sdwan_address}? ")
    sdwan_username = "devnetuser"
    sdwan_password = getpass(f"What is the password for {args.sdwan_address}? (input will be hidden)")
    sdwan_password = "RG!_Yw919_83"
    print()

# Gathering info on inventory from ACI and SD-WAN
if args.aci_address:
    print(f"\033[94mInventory details will be pulled from Cisco APIC {args.aci_address}\033[0m")
    aci_info = lookup_aci_info(args.aci_address, aci_username, aci_password)
    
    # for debug, print results
    print(aci_info)

if args.sdwan_address:
    print(f"\033[94mInventory details will be pulled from Cisco APIC {args.sdwan_address}\033[0m")
    sdwan_info = lookup_sdwan_info(args.sdwan_address, sdwan_username, sdwan_password)
    
    # for debug, print results
    print(sdwan_info)


# Build inventory report data structure
print("\033[92mAssembling network inventory data from output\033[0m")

network_inventory = []

# Add ACI and SD-WAN inventory if needed
if args.aci_address:
    network_inventory += aci_info
if args.sdwan_address:
    network_inventory += sdwan_info

# For debug, print inventory list
print(f"\n\033[96mNetwork_inventory = {network_inventory}\033[0m")


# Generate a CSV File of data

now = datetime.now()
inventory_file = f'{now.strftime("%Y-%m-%d-%H-%M-%S")}_{testbed.name}_inventory.csv'
    
print(f'Writting inventory to file {inventory_file}.')

with open(inventory_file, 'w', newline='') as csvfile:
    inv_writer = csv.writer(csvfile, dialect="excel")
    # Write header row
    inv_writer.writerow(
        ("device_name", 
        "device_os", 
        "software_version", 
        "uptime", 
        "serial_number"
        ))
    
    for device in network_inventory:
        inv_writer.writerow(device)
