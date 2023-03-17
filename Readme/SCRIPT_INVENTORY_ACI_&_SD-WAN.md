# SCRIPT INVENTORY ACI & SD-WAN

In this section we need to reserve our sandboc for ACI Simulator Sandbox V5 in the portal of cisco. [Free](https://devnetsandbox.cisco.com/RM/Topology)

![image](https://user-images.githubusercontent.com/38144008/225805891-07075d98-db4e-43f9-b674-64d19be34a9d.png)

![image](https://user-images.githubusercontent.com/38144008/225861962-67e7d1db-04cb-47bf-a533-32d07928518e.png)


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

![image](https://user-images.githubusercontent.com/38144008/225862214-72fdce0a-ea7e-4c7f-be43-7e6a67cc611f.png)

We need to review the documentation that offer cisco https://developer.cisco.com/docs/sdwan/#!authentication/how-to-authenticate

+ SD-WAN = https://sandbox-sdwan-2.cisco.com
+ Username: devnetuser
+ Password: RG!_Yw919_83

![image](https://user-images.githubusercontent.com/38144008/225851493-d36d66c1-b8d3-4b13-a106-5b495b5d9977.png)

![image](https://user-images.githubusercontent.com/38144008/225851969-4acdf722-7d1b-416f-9663-4b6adf6e0c8d.png)

![image](https://user-images.githubusercontent.com/38144008/225853688-d580abd0-610d-4cd1-b594-e1e46fee6af0.png)

![image](https://user-images.githubusercontent.com/38144008/225854037-3acc57a2-8166-4ef4-923d-07483279788e.png)

# AUTHENTICATION WITH PYTHON ACI
 
 Authentication for Aci in python using the postman flow.
 
 ```python
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
 ```



# AUTHENTICATION WITH PYTHON ACI
 
```python

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


```

Use the command `./network_inventory.py sdn_sandbox_testbed.yaml --aci-address 10.10.20.14 --sdwan-address sandbox-sdwan-2.cisco.com` to run all the solution.

* Where the final result is a file csv with all detail ACI and SD-WAN devices.

![image](https://user-images.githubusercontent.com/38144008/225861781-c0c9ccfc-dae3-4a64-9e13-fbbec852c441.png)





