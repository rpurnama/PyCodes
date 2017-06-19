#Contoh List
contoh_list=['Windows', 
	'Ubuntu',
	'FreeBSD',
	'Solaris',
	'DOS']
	
#Contoh Tuple
contoh_tuple=(0,1,2,3,4,5,6,7,8,9)

#Contoh Dictionary
contoh_dict={'nama':'John Doe',
			'position':'CEO',
			'DoB':'19-Nov-1976',
			'phone':'+6212345678',
			'email':'jdoe@abc.def'}
			
#Cara Menambahkan List
print "Isi list sebelum: ", contoh_list
list_baru = contoh_list + ['LinuxMint','OpenSuse','Slackware']
print "Isi list setelah: ", list_baru
print "\n"

#Cara Menambahkan Tuple
print "Isi tuple sebelum: ", contoh_tuple
tuple_baru = contoh_tuple + (10,11,12,13)
print "Isi tuple setelah: ", tuple_baru
print "\n"

#Cara Menambahkan Dictionary
print "Isi dictionary sebelum", contoh_dict
dict_update = {'education':'B. Eng',
			   'address':'Sunny Vale, CA'}
contoh_dict.update(dict_update)
print "Isi dictionary setelah: ", contoh_dict

