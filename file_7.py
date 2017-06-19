import os

try:
	os.remove('daftar-hadir.txt')
	print "File Deleted..."
except (IOError,OSError),e:
	print "Proses error karena: ",e