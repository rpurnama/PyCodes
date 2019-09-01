#!/user/bin/python2.7
"""
Version	: 0.0 (draft-release)
Author	: Rakhmadian Purnama <rakhmadian.purnama@mastersystem.co.id>
Source	: https://github.com/rpurnama
Required Modules: paramiko, netmiko, scp, pyyaml, pyserial, textfsm
"""

from netmiko import ConnectHandler
import sys

print("Hi, do you really want to delete the configuration?") 
print("Please make sure to backup your device!")
print("-----------------------------------------------------\n")

ip_addr = sys.argv[1]
uid = raw_input("Enter Username: ")
#uid = sys.argv[2]
pwd = raw_input("Enter Password: ")
#pwd = sys.argv[3]

#Load Connection for Cisco IOS-XR
router_xrv = {
	'device_type': 'cisco_xr',
	'host': ip_addr,
	'username': uid,
	'password': pwd,
}

"""
#Load Connection for Cisco IOS
router_xrv = {
	'device_type': 'cisco_ios',
	'host': ip_addr,
	'username': uid,
	'password': pwd,
}
"""

devconnect = ConnectHandler(**router_xrv)

connected_device = devconnect.find_prompt()
print("You are now successfully connected to %s" %connected_device)

cmd_executed = raw_input("Please enter specific command you want to execute: ")
#cmd_executed = ['1st-command','2nd-command', '3rd-command', and so on]

cmd_output = devconnect.send_config_set(cmd_executed)
print(cmd_output)
print("Your command has been executed, well done!\n")

cmd_commit = raw_input("Do you want to commit? (yes/no)")

if cmd_commit == "yes":
	devconnect.commit()
elif cmd_commit == "no":
	print("Command is not commited")
else:
	print("Your option is wrong, dude! Either yes/no ONLY")

#Terminate Connection
devconnect.disconnect()
print("Connection is closed, good bye!!!")
