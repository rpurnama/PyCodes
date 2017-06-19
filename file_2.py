try:
	sebuah_file = open("absen.txt",'w')
	
	print "Name file yang tadi dibuat: ",sebuah_file.name
	print "Mode pembacaan file: ",sebuah_file.mode
	print "Apakah filenya sudah ditutup?",sebuah_file.closed
	
	sebuah_file.write('1. Jajang Surahman, Teknik Informatika, ITB\n')
	sebuah_file.write('2. Angel Corine, Manajemen Bisnis, UNPAD\n')
	sebuah_file.write('3. Tatang Sutartang, Teknik Pertanian, STEKPI\n')
	
	sebuah_file.close()
	print "Apakah filenya sudah ditutup?",sebuah_file.closed
	
except IOError,e:
	print "Proses gagal karena: ",e
	