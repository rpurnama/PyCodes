import telnetlib
import sys
import getpass


def setInterface(intf, ipadd, mask):
	setiface = "network "+intf+"\n ip address "+ipadd+" "+mask		
	
	print "The following configuration will be applied:"
	print '-'*30
	print setiface
	print '-'*30
	q_apply = raw_input('Are you sure with the configuration?(y/n): ')
	if q_apply == 'y':
		print "Configuration SUCCESS!"
	elif q_apply == 'n':
		print "Configuration ABORTED!"
	else:
		print "Configuration ERROR!"	
		
def staticRoute(dest, mask, next_hop):
	route = "route "+dest+" "+mask+" "+next_hop+"\n"
	
def OA57X0():
#OA5710 Configuration Network
	print "Welcome at OA57x0 Network Configuration Menu"		
	print """Available Interface :\n
	1) Ethernet0/0 (LAN Interface)
	2) Ehternet0/1 (WAN-2 Interface)
	"""
	int_opt = raw_input('Please select your interface [1-2]: ')
	if int_opt == "1":
		intf = 'Ethernet0/0'
		ip = raw_input('Please enter IP Address (ex:192.168.1.1) => ')
		mask = raw_input('Please enter Netmask (ex:255.255.255.0) => ')
		setInterface(intf, ip, mask)
	elif int_opt =="2":
		intf = 'Ethernet0/1'
		ip = raw_input('Please enter IP Address (ex:192.168.1.1) => ')
		mask = raw_input('Please enter Netmask (ex:255.255.255.0) => ')
		setInterface(intf, ip, mask)
	else:
		print "Interface not available"
	
	print "\nConfigure Static/Default Route"
	dst_rt = raw_input('Enter route destination or 0.0.0.0 for default route: ')
	dst_msk = raw_input('Enter wilcard mask: ') 
	neighbour = raw_input('Enter next-hop / gateway: ')
	staticRoute(dst_rt, dst_msk, neighbour)
	
def OA58X0():
#OA5850 Configuration Network
	print "Welcome at OA58x0 Network Configuration Menu"		
	print """Available Interface : \n
	1) Ethernet0/0 (WAN-1 Interface)
	2) Ehternet0/1 (WAN-2 Interface)
	3) Ethernet0/2 (LAN Interface)
	"""
	
	int_opt = raw_input('Please select your interface [1-2]: ')
	if int_opt == "1":
		intf = 'Ethernet0/0'
		ip = raw_input('Please enter IP Address (ex:192.168.1.1) => ')
		mask = raw_input('Please enter Netmask (ex:255.255.255.0) => ')
		setInterface(intf, ip, mask)
	elif int_opt =="2":
		intf = 'Ethernet0/1'
		ip = raw_input('Please enter IP Address (ex:192.168.1.1) => ')
		mask = raw_input('Please enter Netmask (ex:255.255.255.0) => ')
		setInterface(intf, ip, mask)
	elif int_opt =="3":
		intf = 'Ethernet0/2'
		ip = raw_input('Please enter IP Address (ex:192.168.1.1) => ')
		mask = raw_input('Please enter Netmask (ex:255.255.255.0) => ')
		setInterface(intf, ip, mask)
	else:
		print "Interface not available"
	
	print "\nConfigure Static/Default Route"
	dst_rt = raw_input('Enter route destination or 0.0.0.0 for default route: ')
	dst_msk = raw_input('Enter wilcard mask: ') 
	neighbour = raw_input('Enter next-hop / gateway: ')
	staticRoute(dst_rt, dst_msk, neighbour)

#Main Menu
welcome = "    Welcome at OmniAccess ESR Configuration Tool    "

print '='*(len(welcome)+2)
print '#'+' '*(len(welcome)-1)+' '+'#'
print '#'+welcome+'#'
print '='*(len(welcome)+2)

print """
These device types which are currently supported.
What's your device type?
1) OmniAccess 57x0 ESR Family
2) OmniAccess 58x0 ESR Family
"""
dev_type = raw_input('Please choose your device type [1-2]: ')
if dev_type =="1":
	OA57X0()
elif dev_type =="2":
	OA58X0()
#Wrong Device Type				
else:
	print "Sorry, your device isn't supported at this moment.\nNo available interface!"
