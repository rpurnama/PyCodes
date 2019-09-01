#!/user/bin/python2.7
"""
Version	: 0.0 (draft-release)
Author	: Rakhmadian Purnama <rakhmadian.purnama@mastersystem.co.id>
Source	: https://github.com/rpurnama
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

router_xrv = {
	'device_type': 'cisco_xr',
	'host': ip_addr,
	'username': uid,
	'password': pwd,
}

devconnect = ConnectHandler(**router_xrv)

connected_device = devconnect.find_prompt()
print("You are now successfully connected to %s" %connected_device)

cmd_executed = raw_input("Please enter specific command you want to execute: ")
#cmd_executed = ['list of commands you want to execute in Cisco IOS-XR']

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
print("Connection closed, good bye!!!")
