try:
	sebuah_file = open("absen.txt",'rb')
	
	print "Nama file: ",sebuah_file.name
	print "Mode pembacaan: ",sebuah_file.mode
	print "Apakah file sudah ditutup?",sebuah_file.closed
	
	print "Isi file:\n"
	for line in sebuah_file:
		print line
		
	print "Posisi pointer pada file: ",sebuah_file.tell()
	print "Kembali lagi ke awal: ",sebuah_file.seek(0,0)
	
	print "Isi file\n"
	for line in sebuah_file:
		print line
		
	print "Posisi pointer pada file: ",sebuah_file.tell()
	
	sebuah_file.close()
	print "Apakah file sudah ditutup?",sebuah_file.closed

except IOError,e:
	print "Proses gagal karena: ",e