#5.Variabel Statis & Variabel Dinamis
#5.1 5 Variabel Statis
class Contoh:
    statis = 0  # variabel statis
    
    def __init__(self):
        Contoh.statis += 1

obj1 = Contoh()
obj2 = Contoh()
print("Jumlah objek:", Contoh.statis)
#5.2 Variabel Dinamis
x = 10
x = "sekarang string"
x = 3.14
print(x)