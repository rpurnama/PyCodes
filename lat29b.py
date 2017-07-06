# lat29b.py

daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']
print("assignment biasa")
daftar_saya = daftar_belanja

del daftar_belanja[0]

print("daftar belanja:", daftar_belanja)
print("daftar saya:",daftar_saya)

print("copy objek daftar belanja menggunakan slice [:]")
daftar_saya = daftar_belanja[:] #membuat copy

del daftar_saya[0]

print("daftar belanja:", daftar_belanja)
print("daftar saya:",daftar_saya)
