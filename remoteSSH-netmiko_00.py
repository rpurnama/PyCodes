from netmiko import ConnectHandler

device = {'device_type':'linux',
		'ip':'192.168.56.101',
		'username':'presales',
		'password':'qwerty123'}
		
koneksi = ConnectHandler(**device)

outcmd = koneksi.send_command('ls -al\n')

print(outcmd)

koneksi.disconnect()