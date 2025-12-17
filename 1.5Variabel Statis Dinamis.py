#variabel statis
class Mahasiswa:
    total_mahasiswa = 0   # variabel statis

    def __init__(self, nama):
        self.nama = nama
        Mahasiswa.total_mahasiswa += 1

    def info(self):
        print("Nama:", self.nama)

# Program utama
m1 = Mahasiswa("Maya")
m2 = Mahasiswa("Dewy")
m3 = Mahasiswa("Ana")

m1.info()
m2.info()
m3.info()

print("Total Mahasiswa:", Mahasiswa.total_mahasiswa)



#variabel dinamis
class Produk:
    def __init__(self, nama, harga):
        self.nama = nama    # variabel dinamis
        self.harga = harga  # variabel dinamis

    def info(self):
        print("Produk:", self.nama)
        print("Harga :", self.harga)

# Program utama
p1 = Produk("Baju", 15000)
p2 = Produk("jilbab", 5000)

p1.info()
print()
p2.info()
