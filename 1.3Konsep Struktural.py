# PROGRAM KONSEP STRUKTURAL PYTHON
# Studi kasus: Pengolahan nilai mahasiswa

# Fungsi untuk menentukan grade
def tentukan_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    else:
        return "D"

# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Array (list) untuk menyimpan data
nama_mahasiswa = []
nilai_mahasiswa = []

# Perulangan untuk input data
for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama  : ")
    nilai = int(input("Nilai : "))

    nama_mahasiswa.append(nama)
    nilai_mahasiswa.append(nilai)

# Menampilkan hasil
print("\n=== HASIL NILAI MAHASISWA ===")
for i in range(jumlah):
    grade = tentukan_grade(nilai_mahasiswa[i])
    print(f"{nama_mahasiswa[i]} | Nilai: {nilai_mahasiswa[i]} | Grade: {grade}")

print("\nProgram selesai dijalankan")
