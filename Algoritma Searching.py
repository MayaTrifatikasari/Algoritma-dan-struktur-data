# ALGORITMA SEARCHING

data = [10, 25, 30, 45, 50]
cari = int(input("Masukkan data yang dicari: "))

ditemukan = False
for i in range(len(data)):
    if data[i] == cari:
        print("Data ditemukan pada indeks ke-", i)
        ditemukan = True
        break

if not ditemukan:
    print("Data tidak ditemukan")
