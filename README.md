# [![image](https://user-images.githubusercontent.com/38144008/225514767-010fa633-9c2e-410a-9734-4fce1372d125.png)](https://youtu.be/N51iZO8GDCc)
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON) [![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/devenv/?id=devenv-vscode-base&GITHUB_SOURCE_REPO=https://github.com/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON)
# SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN

Software defined network ACI & SD-WAN inventory with Python work over requests library to simplify and accelerate the process of collecting and organizing information about network devices. By leveraging the power of Python programming, network administrators can create customized scripts that automate the collection of device data, enabling them to quickly and accurately generate an inventory of all devices on their network. In this scenario we are going to work with sandbox ACI and SD-WAN. 

![image](https://user-images.githubusercontent.com/38144008/225774372-8e471382-1618-4de3-8496-5065fc0a6dc4.png)

In order to generarte a report for SD-WAN AND ACI as initial point is necesary respond this questions:

 
+ Click to Machine Logo to check the video!!! 

+ How can we talk to the controllers?
We are going to use REST API
+ What API are available to retrieve the information?
+ How can we explore and test the APIs?
ACI Inspector and Postman
+ How can we use those APIs in Python?
We are going to work with the library requests
+ How do we add this feature to the inventory script?
Create a New Script for ACI / SD_WAN

* Library to interact: requests, pyATS

|Topics|Description|Title|Notes|
|---|---|---|---|
| INSTALL PYTHON AND DEPENDENCIES | Install Python 3.10.2.  | [INSTALL PYTHON AND DEPENDENCIES](https://github.com/ERICK-ZABALA/SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN/blob/main/Readme/INSTALL_PYTHON_AND_DEPENDENCIES.md) | In this first step you install your Python. |
| INSTALL ANYCONNECT VPN CLIENT | Install VPN Client via CLI  | [INSTALL ANYCONNECT VPN CLIENT](https://github.com/ERICK-ZABALA/SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN/blob/main/Readme/INSTALL_ANYCONNECT_VPN_CLIENT.md) | In this second step you are going to install your vpn anyconnect client. |
| INSTALL GIT | Install GIT via CLI | [INSTALL GIT](https://github.com/ERICK-ZABALA/SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN/blob/main/Readme/INSTALL_GIT.md) | In this step you install git in your environment. |
| SCRIPT INVENTORY ACI & SD-WAN | Script to collect inventory for ACI and SD-WAN | [SCRIPT INVENTORY ACI & SD-WAN](https://github.com/ERICK-ZABALA/SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN/blob/main/Readme/SCRIPT_INVENTORY_ACI_%26_SD-WAN.md) | In this section you are going to generate the inventory using python. |
| SCRIPT TO CREATE A CSV FILE | Script to generate a CSV File | [SCRIPT TO CREATE A CSV FILE](https://github.com/ERICK-ZABALA/SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN/blob/main/Readme/SCRIPT_TO_CREATE_A_CSV_FILE.md) | In this step you are going to dowload the files captured previously via Python. |

# REFERENCES

* Download in your machine [Summer 2021 Devasc-Prep-Network-Inventory-02](https://github.com/hpreston/summer2021-devasc-prep-network-inventory-02.git) maked by Hank Preston, that is a guide if you need help to develop all the code related how to make an inventory.
* [Devnet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology) to test owner Inventory
* Reserve your Sandboc ACI Simulator [here!](https://devnetsandbox.cisco.com/RM/Diagram/Index/390f2dc1-7ca7-44e8-bd7e-f32c0f146ef1)
* [SD-WAN](https://sandboxdnac2.cisco.com/) Online Always Active
* [JSON](https://jsonlint.com/) to test format
