# lat7.py

total_uang = 10000
harga_barang = 5000
diskon = 0.10

# harga barang setelah diskon
harga_barang *= (1 - diskon)

total_uang -= harga_barang

print("total uang = %s" %total_uang)