#![image](https://user-images.githubusercontent.com/38144008/225521047-46cbe5b5-8a35-41fa-bfd3-b0bb31f9045f.png)

# INSTALL PYTHON AND DEPENDENCIES

To install python in your development environment. you can follow these steps.

+ Download Python via console.

`[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz`

+ Extract the downloaded archive by running the following command:

`[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ tar -xvf Python-3.10.2.tgz`

Navigate to the extracted directory by running the following command:

```yaml
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ cd Python-3.10.2

[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ ./configure --enable-optimizations
```

Build and install Python 3.10 using the following command:

```yaml
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ make

[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ sudo make altinstall

[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ python3.10.2 --version
Python 3.10.2

```
NOTA: if you have problem in you environment getting an response as "(main) $ python --version
Python 3.10.4" you need to apply this command to resolve the problem.

```yaml
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT/Python-3.10.2]$ ls /usr/local/bin/python*
/usr/local/bin/python3.10  /usr/local/bin/python3.10-config
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT/Python-3.10.2]$ sudo ln -s /usr/local/bin/python3.10 /usr/local/bin/python3.10.2
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT/Python-3.10.2]$ python --version
Python 3.10.4
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT/Python-3.10.2]$ python3.10 --version
Python 3.10.4
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT/Python-3.10.2]$ python3.10.2 --version
Python 3.10.2

Then you can create your environment normal...
```

# CREATE VENV PYTHON 3.10.2 WITH PyATS

Note: PyATS just available in environments over Linux.

```yaml
[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ python3.10 -m venv assistant

[opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ source assistant/bin/activate

(assistant) [opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ python --version
Python 3.10.2
```
In this environment the version of python is `Python 3.10.2` 
```python

(assistant) [opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ pip list

Package    Version
---------- -------
pip        21.2.4
setuptools 58.1.0
WARNING: You are using pip version 21.2.4; however, version 23.0.1 is available.
You should consider upgrading via the '/home/opc/DEVNET/00_BUILDING-A-TROUBLESHOOTING-ASSISTANT/inventory/bin/python3.10 -m pip install --upgrade pip' command.

(inventory) [opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ pip install --upgrade pip

(inventory) [opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ pip install "scp"
(inventory) [opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ pip install paramiko
(inventory) [opc@jenkins-master 00_BUILDING-A-TROUBLESHOOTING-ASSISTANT]$ pip freeze > requirements.txt
```

# INSTALL TELNET IN LINUX

```bash
[opc@jenkins-master ~]$ sudo dnf install telnet

========================================================================================================================
 Package                 Architecture            Version                           Repository                      Size
========================================================================================================================
Installing:
 telnet                  x86_64                  1:0.17-76.el8                     ol8_appstream                   72 k

Transaction Summary
========================================================================================================================
Install  1 Package

Total download size: 72 k
Installed size: 119 k
Is this ok [y/N]: y
Downloading Packages:
telnet-0.17-76.el8.x86_64.rpm                                                           885 kB/s |  72 kB     00:00
------------------------------------------------------------------------------------------------------------------------
Total                                                                                   833 kB/s |  72 kB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                1/1
  Installing       : telnet-1:0.17-76.el8.x86_64                                                                    1/1
  Running scriptlet: telnet-1:0.17-76.el8.x86_64                                                                    1/1
  Verifying        : telnet-1:0.17-76.el8.x86_64                                                                    1/1

Installed:
  telnet-1:0.17-76.el8.x86_64

Complete!
```

+ Testing telnet in your environment.

```bash
[opc@jenkins-master ~]$ telnet 8.8.8.8 53
Trying 8.8.8.8...
Connected to 8.8.8.8.
Escape character is '^]'.
```

# Configure Nexus 9000

You need to have activated your VPN Client to Sandbox.

```bash
[opc@jenkins-master ~]$ telnet 10.10.20.177
Username: cisco
Password: cisco

~ Nexus 9000:

dist-sw01(config)# username admin password Cisco123 role network-admin
dist-sw01(config)# feature sftp-server
dist-sw01(config)# feature scp-server

```

# Test to pass a File

From your environment development try to send a file to Nexus 9000.

```bash
[opc@jenkins-master ~]$ scp test.py admin@10.10.20.177:      
User Access Verification

(admin@10.10.20.177) Password: Cisco123 
test.py                                                       100%  814     4.1KB/s   00:00    

dist-sw01(config)# dir
       4096    Nov 22 16:59:33 2021  .rpmstore/
       4096    Nov 22 17:00:10 2021  .swtam/
 1339749888    Aug 20 16:21:45 2019  nxos.9.2.4.bin
        814    Mar 13 23:43:28 2023  test.py
          0    Mar 13 19:20:11 2023  platform-sdk.cmd
       4096    Nov 22 17:01:04 2021  scripts/
        221    Nov 22 17:01:47 2021  set_boot.py
       4096    Nov 22 17:01:45 2021  virt_strg_pool_bf_vdc_1/
       4096    Nov 22 17:00:32 2021  virtual-instance/
         59    Nov 22 17:00:24 2021  virtual-instance.conf
```

# REFERENCES
+ [Switches Nexus Supported](https://developer.cisco.com/site/python/) python onbox.
+ [Devnet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology) to test your Nexus9000.
+ [JSON](https://jsonlint.com/) to test format.
