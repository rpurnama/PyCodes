menu_item=0
namelist = []

while menu_item != 9:
	print("----------------------------")
	print("1. Mencetak List")
	print("2. Menambahkan nama ke dalam list")
	print("3. Menghapus nama dari list")
	print("4. Mengubah data dari dalam list")
	print("9. Keluar")
	
	menu_item= int(input("Pilih menu: "))
	if menu_item == 1:
		current = 0
		if len(namelist) > 0:
			while current < len(namelist):
				print(current, ".", namelist[current])
				current = current + 1
		else:
			print("List Kosong")
	elif menu_item == 2:
		name = input("Masukkan nama: ")
		namelist.append(name)
	elif menu_item == 3:
		del_name = input("Nama yang ingin dihapus: ")
		if del_name in namelist:
			#namelist.remove(del_name) dapat digunakan
			item_number = namelist.index(del_name)
			del namelist[item_number]			
			#Kode di atas hanya menghapus nama pertama yang ada.
			
			#Kode di bawah ini menghapus semua nama
			"""
			while del_name in namelist:
				item_number = namelist.index(del_name)
				del namelist[item_number]
			"""
		else:
			print(del_name, "tidak ditemukan")
	elif menu_item == 4:
		old_name = input("Nama apa yang ingin diubah: ")
		if old_name in namelist:
			item_number = namelist.index(old_name)
			new_name = input("Nama baru: ")
			namelist[item_number] = new_name
		else:
			print(old_name, "tidak ditemukan")

print("Selamat tinggal")