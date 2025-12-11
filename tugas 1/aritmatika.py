print("=== Program Aritmatika Sederhana ===")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian   = angka1 * angka2
pembagian   = angka1 / angka2 if angka2 != 0 else "Tidak bisa bagi nol"

print("\nHasil Operasi:")
print("Penjumlahan :", penjumlahan)
print("Pengurangan :", pengurangan)
print("Perkalian   :", perkalian)
print("Pembagian   :", pembagian)
