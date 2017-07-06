# lat10.py
# acak looping

nomor_acak = 77
berjalan = True

print("tebak nomor acak dari 1 - 100")

while berjalan:
	
	tebakan = int(input("Tebakan anda (bil bulat): "))
	
	if tebakan == nomor_acak:
		print("Selamat! tebakan anda benar")
		berjalan = False
	elif tebakan < nomor_acak:
		print("tebakan anda terlalu kecil")
	else:
		print("tebakan anda terlalu besar")
		
else:
	print("Selesai")