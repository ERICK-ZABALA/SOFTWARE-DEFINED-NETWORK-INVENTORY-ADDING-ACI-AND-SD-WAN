# [![image](https://user-images.githubusercontent.com/38144008/225514767-010fa633-9c2e-410a-9734-4fce1372d125.png)](https://youtu.be/7oDCBUMqTSY)

# SOFTWARE-DEFINED-NETWORK-INVENTORY-ADDING-ACI-AND-SD-WAN

Network Automation is becoming increasingly important for managing and maintaining large-scale networks efficiently. If you're working with Cisco Switch Nexus 9000 NX-OS, you might be familiar with the Embedded Event Manager (EEM) and the importance of capturing logs when specific events occur on your interfaces.

![image](https://user-images.githubusercontent.com/38144008/225774372-8e471382-1618-4de3-8496-5065fc0a6dc4.png)

In this project, we'll be exploring the powerful CLI library in Cisco Switch Nexus 9000 NX-OS and leveraging it to build a troubleshooting assistant that can automate the process of capturing logs and storing them in the bootflash. By the end of this project, you'll have a better understanding of how to use EEM, CLI libraries, and automation to streamline your network operations and troubleshoot issues faster. 

In order to generarte a report for SD-WAN AND ACI as initial point is necesary respond this questions:

+ 
+ Click to Machine Logo to check the video!!! 

+ How can we know the status changed?
  Syslog
+ Where run the command?
  Onbox Nexus 9000
+ How to send the command to nexus 9000?
  Using Cli library of Python
+ Where we are going to save the information?
  Bootflash
+ How to xtract the information allocated in the Nexus
  Using SCP


* Library to interact: Cli, scp

|Topics|Description|Title|Notes|
|---|---|---|---|
| INSTALL PYTHON AND DEPENDENCIES | Install Python 3.10.2.  | [INSTALL PYTHON AND DEPENDENCIES](https://github.com/ERICK-ZABALA/BUILDING-A-TROUBLESHOOTING-ASSISTANT/blob/main/Readme/INSTALL_PYTHON_AND_DEPENDENCIES.md) | In this first step you install your Python. |
| INSTALL ANYCONNECT VPN CLIENT | Install VPN Client via CLI  | [INSTALL ANYCONNECT VPN CLIENT](https://github.com/ERICK-ZABALA/BUILDING-A-TROUBLESHOOTING-ASSISTANT/blob/main/Readme/INSTALL%20_VPN_CLIENT_ANYCONNECT.md) | In this second step you are going to install your vpn anyconnect client. |
| INSTALL GIT | Install GIT via CLI | [INSTALL GIT](https://github.com/ERICK-ZABALA/BUILDING-A-TROUBLESHOOTING-ASSISTANT/blob/main/Readme/INSTALL_GIT.md) | In this step you install git in your environment. |
| SCRIPT ASSISTANT | Script Assistant onbox in Nexus 9000 | [SCRIPT ASSISTANT ONBOX](https://github.com/ERICK-ZABALA/BUILDING-A-TROUBLESHOOTING-ASSISTANT/blob/main/Readme/SCRIPT_ASSISTANT.md) | In this step you are going to create the code to capture information if exist an event. |
| SCRIPT TO EXTRACT FOLDER | Script files using scp in Python | [EXTRACT NEXUS 9000 FILES](https://github.com/ERICK-ZABALA/BUILDING-A-TROUBLESHOOTING-ASSISTANT/blob/main/Readme/SCRIPT_SCP.md) | In this step you are going to dowload the files captured previously via Python. |

# REFERENCES

+ [Devnet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology) to test owner Inventory
+ [JSON](https://jsonlint.com/) to test format
