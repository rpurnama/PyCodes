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

#Cara Hapus Elemen List
print "Isi list sebelum: ", contoh_list
del contoh_list[4]
print "Isi list setelah: ", contoh_list
print "\n"

#Cara Hapus Elemen Tuple
print "Isi tuple sebelum: ", contoh_tuple
print "Elemen tuple tidak dapat dihapus"
print "\n"

#Cara Hapus Elemen Dictionary
print "Isi dictionary sebelum: ", contoh_dict
del contoh_dict['email']
print "Isi dictionary setelah: ", contoh_dict

