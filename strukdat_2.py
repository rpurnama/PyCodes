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

#Cara mengakses elemen.
print("Cara mengakses salah satu elemen")
print("--------------------------------")
print contoh_list[3]
print contoh_tuple[3]
print contoh_dict['phone']
print "\n"

#Cara mengakses beberapa elemen, hanya list & tuple yang bisa diakses dalam range elemen.
print("Cara mengakses beberapa elemen")
print("------------------------------")
print contoh_list[1:3]
print contoh_tuple[4:7]
print "\n"

#Cara mengakses elemen menggunakan looping
for a in contoh_list:
	print a
print "\n"

for b in contoh_tuple:
	print b
print "\n"
	
for c in contoh_dict:
	print c,':',contoh_dict[c]
	


