import os

try:
	os.rename('absen.txt','daftar-hadir.txt')
	print "Nama file sudah diubah..."

except (IOError, OSError),e:
	print "Proses error karena: ",e