#Contoh List.
contoh_list=['Windows', 
	'Ubuntu',
	'FreeBSD',
	'Solaris',
	'DOS']
	
#Contoh Tuple.
contoh_tuple=(0,1,2,3,4,5,6,7,8,9)

#Contoh Dictionary.
contoh_dict={'nama':'John Doe',
			'position':'CEO',
			'DoB':'19-Nov-1976',
			'phone':'+6212345678',
			'email':'jdoe@abc.def'}
			
#Contoh mengupdate elemen data pada List
print "Ubah Data pada List"
i = input('Enter Index: ')
print "Original List:",contoh_list[i]
#print contoh_list
elemen_val = raw_input('New Elemen: ')
contoh_list[i] = elemen_val
print "New List: ", contoh_list
print "\n"

#Contoh mengupdate elemen data pada Tuple, NOT AVAILABLE!

#Contoh mengupdate elemen data pada dictionary
print "Ubah Data pada Dictionary"
print contoh_dict
keyidx = raw_input('Key Index: ')
contoh_dict[keyidx] = raw_input('Masukkan Data Baru: ')
print contoh_dict

