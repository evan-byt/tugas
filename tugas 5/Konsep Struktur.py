#3.konsep struktur
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

m1 = Mahasiswa("Evan", "D0425321", 89)
print(m1.nama, m1.nim, m1.nilai)