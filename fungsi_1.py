def fungsi_tanpa_parameter():
	for i in range(1,5):
		print "looping ke - ",i
		
def fungsi_berparameter(batas_akhir):
	for i in range(1, batas_akhir):
		print "looping ke - ",i
		
print "Contoh penggunaan fungsi tanpa parameter:"
print "Hasil: ", fungsi_tanpa_parameter()

print "\n\n"

print "Contoh penggunaan fungsi berparamenter:"
print "Hasil: ", fungsi_berparameter(10)