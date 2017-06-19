#Contoh List
sebuah_list=['Windows', 
	'Ubuntu',
	'FreeBSD',
	'Solaris',
	'DOS']
	
#Contoh Tuple
sebuah_tuple=(0,1,2,3,4,5,6,7,8,9)

#Contoh Dictionary
sebuah_dictionary={'nama':'John Doe',
			'position':'CEO',
			'DoB':'19-Nov-1976',
			'phone':'+6212345678',
			'email':'jdoe@abc.def'}

#Menambahkan elemen baru
print "menambahkan elemen baru: \n"
print sebuah_list
list_baru = sebuah_list + ['PC Linux OS', 'Blankon','IGOS','OpenSUSE']
print list_baru
print "\n"

print sebuah_tuple
tuple_baru = sebuah_tuple
print tuple_baru
print "\n"

print sebuah_dictionary
dictionary_baru = {'telp':'0212345678', 'alamat':'Depok, Jawa Barat'}
print sebuah_dictionary
print "\n\n"

#membadingkan yang lama dengan yang baru
print "membandingkan yang lama dengan yang baru: \n"
print "sebuah_list banding list_baru: ", cmp(sebuah_list, list_baru)
print "sebuah_tuple banding tuple_baru: ", cmp(sebuah_tuple, tuple_baru)
print "sebuah_dictionary banding dictionary_baru: ",cmp(sebuah_dictionary, dictionary_baru)

print "\n\n"

#mengetahu panjang list, tuple, dan dictionary
print "mengetahui panjang list, tuple, dan dictionary: \n"
print "panjang sebuah_list: ", len(sebuah_list)
print "panjang sebuah_tuple: ", len(sebuah_tuple)
print "panjang sebuah_dictionary: ", len(sebuah_dictionary)

print "\n\n"

#mengubah list, tuple, dictionary menjadi string
print "mengubah list, tuple, dictionary menjadi string: \n"
print str(sebuah_list), 'memiliki panjang karakter: ', len(str(sebuah_list))
print str(sebuah_tuple), 'memiliki panjang karakter: ', len(str(sebuah_tuple))
print str(sebuah_dictionary), 'memiliki panjang karakter: ', len(str(sebuah_dictionary))

#mencari nilai MAX dan MIN
print "mencari nilai max dan min: \n"
print "coba periksa sebuah_list:"
print "max: ", max(sebuah_list)
print "min: ", min(sebuah_list)
print "\n"

print "coba periksa sebuah_tuple:"
print "max: ", max(sebuah_tuple)
print "min: ", min(sebuah_tuple)
print "\n"

print "coba periksa sebuah_dictionary:"
print "max: ", max(sebuah_dictionary)
print "min: ", min(sebuah_dictionary)
print "\n"

#mengubah list ke tuple dan sebaliknya
print "mengubah list ke tuple:"
print "semula:", sebuah_list
print "menjadi:",tuple(sebuah_list)
print "\n"

print "mengubah tuple ke list:"
print "semula:", sebuah_tuple
print "menjadi:", list(sebuah_tuple)
