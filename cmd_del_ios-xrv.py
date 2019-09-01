from netmiko import ConnectHandler
import sys

print("Hi, do you really want to delete the configurations?") 
print("Please make sure to backup your device configuration!")
print("-----------------------------------------------------\n")

ip_addr = sys.argv[1]
uid = raw_input("Enter Username: ")
pwd = raw_input("Enter Password: ")

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
