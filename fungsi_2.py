def fungsi_tanpa_parameter():
	temp = 0
	for i in range(1,5):
		temp = temp + i
	return temp
	
def fungsi_berparameter(batas_akhir):
	temp = 0
	for i in range(1, batas_akhir):
		temp = temp + i
	return temp
	
print "Contoh penggunaan fungsi tanpa parameter:"
print "Hasil: ",fungsi_tanpa_parameter()
print "Hasil: ",fungsi_tanpa_parameter()
print "Hasil: ",fungsi_tanpa_parameter()

print "\n\n"

print "Contoh penggunaan fungsi berparameter:"
print "Hasil : ",fungsi_berparameter(15)
print "Hasil : ",fungsi_berparameter(20)
print "Hasil : ",fungsi_berparameter(25)