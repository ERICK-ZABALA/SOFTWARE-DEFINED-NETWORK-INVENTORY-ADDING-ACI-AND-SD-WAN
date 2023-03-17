# SCRIPT INVENTORY ACI & SD-WAN

In this section we need to reserve our sandboc for  ACI Simulator Sandbox V5 in the portal of cisco. [Free](https://devnetsandbox.cisco.com/RM/Topology)

![image](https://user-images.githubusercontent.com/38144008/225805891-07075d98-db4e-43f9-b674-64d19be34a9d.png)

# CISCO Inspector ACI

+ Login to the portal web https://10.10.20.14/ using the credentials [ACI](https://devnetsandbox.cisco.com/sandbox-instructions/ACI_Sim/APIC-Simulator-Reservation-Instructions.pdf)

+ We are going to ACI and navegate to Pod > Node > General

![image](https://user-images.githubusercontent.com/38144008/225823221-787cdc57-ce28-4128-bdc2-a03cecb6d6e5.png)

Check this parameters: Up Time and Firmware.

![image](https://user-images.githubusercontent.com/38144008/225828556-a58159b3-56b0-40a1-9c58-71c9684c41b4.png)

![image](https://user-images.githubusercontent.com/38144008/225828591-dff2634e-8cbd-49e8-b524-788ebe9430f0.png)

+ We are going to see our Inspector ACI > help > ACI Inspector 

![image](https://user-images.githubusercontent.com/38144008/225821740-8182b869-7bc6-4fa9-8612-cb568055b5e3.png)

![image](https://user-images.githubusercontent.com/38144008/225821800-af52870c-8c39-41c2-9836-e91d678df6fa.png)

# POSTMAN ANALYSING 

To generate authentication review this [document](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/1-x/api/rest/b_APIC_RESTful_API_User_Guide/performing_common_tasks.html#reference_07235E7E5C624CA2A514D9E0EEEE065F)

Sending first Post to receive a token.

![image](https://user-images.githubusercontent.com/38144008/225829950-7593f130-564c-4cb0-aaa2-b727d1cd600e.png)

The token is used in the APIC-Cokkie 

![image](https://user-images.githubusercontent.com/38144008/225841779-4d0cb210-ec7e-405f-9964-880c9943ee1c.png)

![image](https://user-images.githubusercontent.com/38144008/225841939-8e30807c-eca3-4988-89b3-1d28ace8df96.png)

![image](https://user-images.githubusercontent.com/38144008/225844156-76ab34c2-77d9-40e1-beb4-15e741ed5b79.png)

# SD-WAN

We need to review the documentation that offer cisco https://developer.cisco.com/docs/sdwan/#!authentication/how-to-authenticate

SD-WAN = https://sandbox-sdwan-2.cisco.com
username: devnetuser
password: RG!_Yw919_83

![image](https://user-images.githubusercontent.com/38144008/225851493-d36d66c1-b8d3-4b13-a106-5b495b5d9977.png)

![image](https://user-images.githubusercontent.com/38144008/225851969-4acdf722-7d1b-416f-9663-4b6adf6e0c8d.png)










