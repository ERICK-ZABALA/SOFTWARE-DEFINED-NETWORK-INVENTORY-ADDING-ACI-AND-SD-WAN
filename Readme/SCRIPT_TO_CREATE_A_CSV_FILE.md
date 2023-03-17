
# Generate a CSV File


```python
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
```
![image](https://user-images.githubusercontent.com/38144008/225864464-9929a547-b775-4930-953e-a3490d2f1394.png)


# REFERENCES

* Download in your machine [Summer 2021 Devasc-Prep-Network-Inventory-02](https://github.com/hpreston/summer2021-devasc-prep-network-inventory-02.git) maked by Hank Preston, that is a guide if you need help to develop all the code related how to make an inventory.
* [Devnet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology) to test owner Inventory
* Reserve your Sandboc ACI Simulator [here!](https://devnetsandbox.cisco.com/RM/Diagram/Index/390f2dc1-7ca7-44e8-bd7e-f32c0f146ef1)
* [SD-WAN](https://sandboxdnac2.cisco.com/) Online Always Active
* [JSON](https://jsonlint.com/) to test format
