# PERANCANGAN ARRAY, STRUKTUR, DAN UNION

# 1. Perancangan Array (List)
nilai = [88, 95, 90, 85]
print("Array Nilai:", nilai)

# Menghitung rata-rata
rata_rata = sum(nilai) / len(nilai)
print("Rata-rata Nilai:", rata_rata)

# 2. Perancangan Struktur (menggunakan class)
class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

    def tampilkan(self):
        print("\nData Mahasiswa")
        print("NIM   :", self.nim)
        print("Nama  :", self.nama)
        print("Nilai :", self.nilai)

# Membuat objek struktur
mhs1 = Mahasiswa("D0425331", "Maya", nilai)
mhs1.tampilkan()

# 3. Perancangan Union (gabungan data)
kelas_a = {"Indri", "Ana", "Marna"}
kelas_b = {"Cya", "Tya", "Rahma"}

gabungan = kelas_a.union(kelas_b)

print("\nKelas A:", kelas_a)
print("Kelas B:", kelas_b)
print("Union  :", gabungan)
