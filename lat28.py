# lat28.py

daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']
nama = 'budi'

print("Barang 0 =", daftar_belanja[0])
print("Barang 1 =", daftar_belanja[1])
print("Barang 2 =", daftar_belanja[2])
print("Barang 3 =", daftar_belanja[3])

print("Barang -1 =", daftar_belanja[-1])
print("Barang -2 =", daftar_belanja[-2])

print("Karakter 0 =", nama[0])

#Slicing pada list
print("Barang 1 ke 3:", daftar_belanja[1:3])
print("Barang 2 ke terakhir:", daftar_belanja[2:])
print("Barang 1 ke -1:", daftar_belanja[1:-1])
print("Barang dari awal ke akhir:", daftar_belanja[:])

# Slicing pada string
print("Karakter 1 ke 3:", nama[1:3])
print("Karakter 2 ke terakhir:", nama[2:])
print("Karakter 1 ke -1:", nama[1:-1])
print("Karakter dari awal ke akhir:", nama[:])