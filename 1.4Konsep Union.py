# KONSEP UNION (GABUNGAN) MENGGUNAKAN SET

# Data himpunan
mahasiswa_a = {"Maya", "Tya", "Cia", "Agus"}
mahasiswa_b = {"Indri", "Marna", "Dewy", "Ana"}

# Menampilkan data awal
print("Kelompok A :", mahasiswa_a)
print("Kelompok B :", mahasiswa_b)

# Union menggunakan operator |
gabungan1 = mahasiswa_a | mahasiswa_b
print("\nUnion dengan operator | :")
print(gabungan1)

# Union menggunakan method union()
gabungan2 = mahasiswa_a.union(mahasiswa_b)
print("\nUnion dengan method union():")
print(gabungan2)

# Union lebih dari dua set
mahasiswa_c = {"Gina", "Hani", "Andi"}
gabungan_semua = mahasiswa_a.union(mahasiswa_b, mahasiswa_c)

print("\nUnion tiga set:")
print(gabungan_semua)

# Union menggunakan perulangan
hasil_union = set()
for data in mahasiswa_a:
    hasil_union.add(data)
for data in mahasiswa_b:
    hasil_union.add(data)

print("\nUnion menggunakan perulangan:")
print(hasil_union)
