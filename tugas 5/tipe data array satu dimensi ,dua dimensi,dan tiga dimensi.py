#2. Tipe data array Satu Dimensi, Dua Dimansi, dan Tiga Dimensi

#2.1 Array 1 Dimensi
array1 = [10, 20, 30, 40, 50]

#print(array1)
#print("Elemen index ke-2:", array1[2])   # 30

#contoh
#nilai seorang mahasiswa di 3 matakuliah
hewan = ['kucing', 'ayam', 'kerbau', 'kuda']

#nilai matakuliah ke-3
print(hewan[2])

#2.2 Array 2 Dimensi
array2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(array2)
#print("Elemen baris ke-2 kolom ke-3:", array2[1][2])  # 6

#contoh 
#buah yang dijual di 3 toko
buah = [
    ['apel', 'jeruk', 'anggur', 'timun'],
    ['pepaya', 'mangga', 'jambu', 'pisang'],
    ['semangka', 'srikaya', 'strowbery', 'cery']
]

# buah yang dijual di toko ke-3
print(buah[2])
# buah yang dijual di toko ke-3 buah ke-4
print(buah[2][3])
#2.3 Array 3 Dimensi
array3 = [
    [
        [1, 2], 
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

#print(array3)
#print("Elemen layer ke-2 baris ke-1 kolom ke-2:", array3[1][0][1])  # 6

#contoh
#pengelompokan hewan berdasarkan jenis dan tempat tinggalnya
hewan = [
    [ #hewan yang hidup di darat
        ['harimau', 'singa', 'macan'], #karnivora
        ['kerbau', 'kambing', 'sapi']  #herbivora
    ],
    [ #hewan yang hidup di air
        ['paus', 'hiu', 'piranha'], #karnivora
        ['nila', 'bandeng', 'tawes'] #herbivora
    ]

]

print(hewan[0]) #untuk hewan yang hidup di darat
print(hewan[1][0]) #untuk hewan yang hidup di air berjenis karnivora
print(hewan[0][1][2]) #untuk hewan yang hidup di darat berjenis herbivora pada baris ke-3
