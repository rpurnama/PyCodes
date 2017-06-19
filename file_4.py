#Cara membaca isi file secara per-baris

try:
	sebuah_file = open("absen.txt",'r')
	
	print "Nama file: ", sebuah_file.name
	print "Mode pembacaan file: ", sebuah_file.mode
	print "Status file close?", sebuah_file.closed
	
	print "Isi file:\n"
	
	for i in sebuah_file:
		print i
	
	print "Posisi pointer pada file: ",sebuah_file.tell()
	
	sebuah_file.close()
	print "Status file close?",sebuah_file.closed
except:
	print "Proses gagal karena: ",e