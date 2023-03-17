
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

