try:
	angka1 = float(raw_input('Angka ke-1: '))
	angka2 = float(raw_input('Angka ke-2: '))

	try:
		print "Hasil perhitungan: ",angka1/angka2
	except ZeroDivisionError,e:
		print "Hasil proses perhitungan gagal karena: ",e

except ValueError,e:
	print "Proses input gagal karena: ",e

print "Proses cetak ini masih dapat dijalankan"