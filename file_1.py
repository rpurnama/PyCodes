try:
	sebuah_file = open("absen.txt",'w')
	
	print "Nama file yang tadi dibuat: ",sebuah_file.name
	print "Mode pembacaan file: ",sebuah_file.mode
	print "Apakah filenya sudah ditutup?",sebuah_file.closed
	
	sebuah_file.close()
	print "Apakah filenya sudah ditutup?",sebuah_file.closed
	
except IOError,e:
	print "Proses gagal karena: ",e