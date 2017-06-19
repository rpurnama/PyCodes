def sebuah_fungsi(sebuah_list):
	sebuah_list = [1,2,3,4,5]
	print sebuah_list

def sebuah_fungsi_lainnya(sebuah_list):
	sebuah_list.append([10,20,30])
	print sebuah_list

ini_list = [10,20,30]
sebuah_list = [100,200,300]

print "Apakah ini_list berubah?"
print ini_list
sebuah_fungsi(ini_list)
print ini_list
print ini_list
sebuah_fungsi_lainnya(ini_list)
print ini_list

print "Apakah sebuah_list berubah?"
print sebuah_list
sebuah_fungsi(sebuah_list)
print sebuah_list
print sebuah_list
sebuah_fungsi_lainnya(sebuah_list)
print sebuah_list