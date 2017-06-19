#Cara membaca isi file secara keseluruhan

try:
	sebuah_file = open("absen.txt",'r')
	
	print "Nama file yang tadi dibuat: ",sebuah_file.name
	print "Mode pembacaan file: ",sebuah_file.mode
	print "Apakah filenya sudah ditutup?",sebuah_file.closed
	
	print "Isi file:\n", sebuah_file.read()
	print "Posisi pointer pada file: ",sebuah_file.tell()
	
	sebuah_file.close()
	print "Apakah filenya sudah ditutup?",sebuah_file.closed

except IOError,e:
	print "Proses gagal karena: ",e