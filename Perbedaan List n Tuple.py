# Contoh List
Nama  = ["Ana", "Saleha", "Kristia"]
print("List sebelum diubah :", Nama)

# Mengubah isi list
Nama[1] = "Ana"
Nama.append("Saleha")

print("List setelah diubah :", Nama)


# Contoh Tuple
kendaraan = ("Motor", "Mobil", "Sepeda")
print("\nTuple awal           :", kendaraan)

# Coba mengubah tuple
try:
    kendaraan[0] = "Kapal"
except TypeError:
    print("Tuple tidak bisa diubah!")


# Ringkasan perbedaan
print("\nKesimpulan:")
print("- List  dapat diubah")
print("- Tuple tidak dapat diubah")
