# lat9.py

nomor_acak = 7
print("tebak nomor acak dari 1 - 10")

# "raw_input" digunakan untuk mendapatkan input dari pengguna
# "int" digunakan untuk konversi tipe data dari "str" ke "int"

tebakan = int(input("Tebakan anda (bil bulat): "))

if tebakan == nomor_acak:
	print("Selamat! tebakan anda benar")
	print("tapi tidak ada hadiah untuk anda :(")
elif tebakan < nomor_acak:
	print("tebakan terlalu kecil")
else:
	print("tebakan anda terlalu besar")
	
print("Finish!")