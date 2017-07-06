# lat27.py

# ba, singkata buku alamat
ba = {'guido':'guido@python.org',\
		'brandon':'brandon@rhodesmill.org',\
		'spammer':'spammer@domain.com'}
		
print("alamat email guido:", ba['guido'])

# menghapus item
del ba['spammer']

print("ada %s kontak di buku alamat" %len(ba))

for nama, email in ba.items():
	print("%s, email: %s" %(nama, email))

# tambah entry
ba['jacob'] = 'jacob@jacobian.org'

if 'jacob' in ba:
	print("Email jacob di", ba['jacob'])