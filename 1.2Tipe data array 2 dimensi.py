# Contoh Array 2 Dimensi di Python

# Membuat array 2 dimensi (list of lists)
nilai = [
    [80, 85, 90],
    [75, 88, 92],
    [60, 70, 78]
]

# Menampilkan seluruh array
print("Data Nilai:")
for baris in nilai:
    print(baris)

# Mengakses elemen tertentu
print("Nilai baris ke-2 kolom ke-3:", nilai[1][2])

# Mengubah elemen
nilai[0][1] = 95
print("Setelah diubah:")
for baris in nilai:
    print(baris)
